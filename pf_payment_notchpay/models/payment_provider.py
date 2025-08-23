import logging
import pprint

import requests
from werkzeug.urls import url_join

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

from odoo.addons.payment import utils as payment_utils
from odoo.addons.payment.const import REPORT_REASONS_MAPPING


_logger = logging.getLogger(__name__)


SUPPORTED_CURRENCIES = ["XAF"]

DEFAULT_PAYMENT_METHOD_CODES = {"cm.mtn", "cm.orange"}


class PaymentProvider(models.Model):
    _inherit = "payment.provider"

    code = fields.Selection(
        selection_add=[("notchpay", "Notchpay")],
        ondelete={"notchpay": "set default"},
    )
    notchpay_public_key = fields.Char(
        string="Notchpay Public Key",
        help="The API key of your Notchpay account",
        required_if_provider="notchpay",
    )

    ###########################################################################
    #                          BUSINESS LOGIC                                 #
    ###########################################################################
    @api.model
    def _get_compatible_providers(
        self, *args, is_validation=False, report=None, **kwargs
    ):
        """Override of `payment` to filter out Notchpay providers for validation operations."""
        providers = super()._get_compatible_providers(
            *args, is_validation=is_validation, report=report, **kwargs
        )

        if is_validation:
            unfiltered_providers = providers
            providers = providers.filtered(lambda p: p.code != "notchpay")
            payment_utils.add_to_report(
                report,
                unfiltered_providers - providers,
                available=False,
                reason=REPORT_REASONS_MAPPING["validation_not_supported"],
            )
        return providers
    
    def _get_supported_currencies(self):
        supported_currencies = super()._get_supported_currencies()
        if self.code == "notchpay":
            supported_currencies = supported_currencies.filtered(
                lambda c: c.name in SUPPORTED_CURRENCIES
            )
        return supported_currencies
    
    def _get_default_payment_method_codes(self):
        default_codes = super()._get_default_payment_method_codes()
        if self.code != "notchpay":
            return default_codes
        return DEFAULT_PAYMENT_METHOD_CODES
    

    ###########################################################################
    #                          MAKE REQUEST TO NOTCHPAY                       #
    ###########################################################################
    def _notchpay_make_request(self, endpoint, payload=None, method="POST"):
        """Make a request to Notchpay API at a specified endpoint

        :param str endpoint: The endpoint to reach for the request
        :param dict payload: The payload of the request.
        :param str method: The HTTP method of the request.
        :return: JSON content of the response, type dict
        :raise ValidationError: If an HTTP error occurs.
        """
        self.ensure_one()

        url = url_join("https://api.notchpay.co/", endpoint)
        headers = {
            "Authorization": self.notchpay_public_key,
            "Accept": "application/json",
        }
        try:
            if method == "GET":
                response = requests.get(
                    url, params=payload, headers=headers, timeout=10
                )
            else:
                response = requests.post(url, data=payload, headers=headers, timeout=10)
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError:
                _logger.exception(
                    "Invalid API request at %s with data:\n%s", url, pprint.pformat(payload),
                )
                raise ValidationError(
                    "Notchpay: "
                    + _(
                        "The communication with the API failed. Notchpay gave us the following "
                        "information: '%s'",
                        response.json().get("message", ""),
                    )
                )
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            _logger.exception("Unable to reach endpoint at %s", url)
            raise ValidationError(
                "Notchpay: " + _("Could not establish the connection to the API.")
            )
        return response.json()
