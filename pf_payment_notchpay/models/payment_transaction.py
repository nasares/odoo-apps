import logging
import pprint

from werkzeug import urls

from odoo import _, fields, models
from odoo.exceptions import ValidationError

from odoo.addons.payment import utils as payment_utils
from odoo.addons.pf_payment_notchpay.controllers.main import NotchpayController


_logger = logging.getLogger(__name__)


PROVIDER_CODE = "notchpay"

PAYMENT_METHODS_MAPPING = {"om": "Orange Money", "momo": "MTN Mobile Money"}

PAYMENT_STATUS_MAPPING = {
    "complete": "complete",
    "pending": "pending",
    "processing": "processing",
    "failed": "failed",
    "canceled": "canceled",
    "expired": "expired",
}


class PaymentTransaction(models.Model):
    _inherit = "payment.transaction"

    notchpay_callback_url = fields.Char()

    ###########################################################################
    #                   TRANSACTION BUSINESS LOGIC                            #
    ###########################################################################
    def _get_specific_rendering_values(self, processing_values):
        """ Override of payment to return Notchpay-specific rendering values.

        :param dict processing_values: The values of the transaction
        :return: The dict of provider-specific processing values.
        """
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != PROVIDER_CODE:
            return res

        # Initialize the payment and retrieve the payment link data
        base_url = self.provider_id.get_base_url()
        payload = {
            "email": self.partner_email,
            "currency": self.currency_id.name,
            "amount": self.amount,
            "phone": self.partner_phone,
            "reference": self.reference,
            "description": f"Payment of SO {self.sale_order_ids.mapped('name')}",
            "callback": urls.url_join(base_url, NotchpayController._return_url),
        }
        payment_link_data = self.provider_id._notchpay_make_request(
            "payments/initialize", payload=payload
        )

        # Extract the payment link URL and put it in the payment form
        rendering_values = {
            "api_url": payment_link_data["authorization_url"],
        }
        return rendering_values

    ###########################################################################
    #                          PAYMENT HTTP REQUEST                           #
    ###########################################################################
    def _send_payment_request(self):
        """ Override of payment to send a payment request to Notchpay.

        Note: self.ensure_one()

        :return: None
        :raise UserError: If the transaction is not linked to a token.
        """
        super()._send_payment_request()
        if self.provider_code != PROVIDER_CODE:
            return

        # Prepare the payment request for Notchpay.
        first_name, last_name = payment_utils.split_partner_name(self.partner_name)
        base_url = self.provider_id.get_base_url()
        data = {
            "token": self.token_id.provider_ref,
            "email": self.token_id.notchpay_customer_email,
            "amount": self.amount,
            "currency": self.currency_id.name,
            "country": self.company_id.country_id.code,
            "tx_ref": self.reference,
            "first_name": first_name,
            "last_name": last_name,
            "ip": payment_utils.get_customer_ip_address(),
            "redirect_url": urls.url_join(
                base_url, NotchpayController._auth_return_url
            ),
        }

        # Make the payment request to Notchpay
        response_content = self.provider_id._notchpay_make_request(
            "payments/initialize", payload=data
        )

        # Handle the payment request response.
        _logger.info(
            "payment request response for transaction with reference %s:\n%s",
            self.reference, pprint.pformat(response_content)
        )
        self._handle_notification_data(PROVIDER_CODE, response_content['data'])


    ###########################################################################
    #                          PAYMENT NOTIFICATIONS                          #
    ###########################################################################
    def _get_tx_from_notification_data(self, provider_code, notification_data):
        """Override payment to find the transaction based on Notchpay data.

        :param str provider_code: the payment provider's code for the transaction
        :param dict notification_data: The notification data sent by the provider
        :return: The transaction if found (recordset of `payment.transaction`)
        :raise ValidationError: If inconsistent data were received.
        :raise ValidationError: If the data match no transaction.
        """
        tx = super()._get_tx_from_notification_data(provider_code, notification_data)
        if provider_code != PROVIDER_CODE or len(tx) == 1:
            return tx

        reference = notification_data.get("reference")
        tx_reference = notification_data.get("trxref")
        if not reference:
            raise ValidationError("Notchpay: " + _("Received data with missing reference."))

        tx = self.search(
            [("reference", "=", tx_reference), ("provider_code", "=", PROVIDER_CODE)]
        )
        if not tx:
            raise ValidationError(
                "Notchpay: "
                + _("No transaction found matching reference %s.", reference)
            )
        return tx

    def _process_notification_data(self, notification_data):
        """Override of payment to process the transaction based on Notchpay data.

        Note: self.ensure_one()

        :param dict notification_data: The notification data sent by the provider.
        :return: None
        :raise ValidationError: If inconsistent data were received.
        """
        super()._process_notification_data(notification_data)
        if self.provider_code != PROVIDER_CODE:
            return

        # Payment verification
        verification_response_content = self.provider_id._notchpay_make_request(
            "payments",
            payload={"reference": notification_data.get("reference")},
            method="GET",
        )
        verified_data = verification_response_content["items"]
        verified_data = [
            data
            for data in verification_response_content.get("items")
            if data.get("reference") == notification_data.get("reference")
        ]

        # Update the provider reference.
        try:
            self.provider_reference = verified_data[0]["reference"]
        except IndexError:
            # Error can happen when the transaction data is not yet sent back
            # by Notchpay. The best way to manage that is to use webhook
            # Do not hesitate to contact us for support
            reference = notification_data.get("reference")
            trxref = notification_data.get("trxref")
            notchpay_trxref = notification_data.get("notchpay_trxref")
            status = notification_data.get("status")
            callback_url = f"/payment/notchpay/return?reference={reference}&trxref={trxref}&notchpay_trxref={notchpay_trxref}&status={status}"
            
            # Store what we have and mark as pending
            self.provider_reference = reference or trxref or notchpay_trxref
            self.state = 'pending'
            self.notchpay_callback_url = callback_url
            
            message = f"Payment processed but API response not ready yet. " \
                    f"Check transaction manually or contact us for support. " \
                    f"Callback: {callback_url}"
            
            _logger.warning("Notchpay API not ready for reference %s", reference)
            return message


        # Update payment method
        payment_method_type = verified_data[0].get("payment_method")

        payment_method = self.env["payment.method"]._get_from_code(
            payment_method_type, mapping=PAYMENT_METHODS_MAPPING
        )
        self.payment_method_id = payment_method or self.payment_method_id

        # Update payment status
        payment_status = verified_data[0]["status"].lower()
        if payment_status in PAYMENT_STATUS_MAPPING["pending"]:
            self.provider_reference = notification_data.get("authorization_url")
            self._set_pending()
        elif payment_status in PAYMENT_STATUS_MAPPING["complete"]:
            self._set_done()
        elif payment_status in PAYMENT_STATUS_MAPPING["canceled"]:
            self._set_canceled()
        elif payment_status in PAYMENT_STATUS_MAPPING["failed"]:
            self._set_error(
                _(
                    "An error occurred during the processing of your payment (status %s). Please try "
                    "again.",
                    payment_status,
                )
            )
        else:
            _logger.warning(
                "Received data with invalid payment status (%s) for transaction with reference %s.",
                payment_status,
                self.reference,
            )
            self._set_error(
                "Notchpay: " + _("Unknown payment status: %s", payment_status)
            )
