import json
import logging
import pprint

from odoo import http
from odoo.http import request


_logger = logging.getLogger(__name__)


class NotchpayController(http.Controller):
    _return_url = "/payment/notchpay/return"
    _auth_return_url = "/payment/notchpay/auth_return"

    @http.route(_return_url, type="http", methods=["GET"], auth="public")
    def notchpay_return_from_checkout(self, **data):
        """Process the notification data sent by Notchpay after redirection 
        from checkout.
        """
        _logger.info(
            "Handling redirection from Notchpay with data:\n%s", pprint.pformat(data)
        )

        # Handle the notification data.
        if data.get("status") != "canceled":
            request.env["payment.transaction"].sudo()._handle_notification_data(
                "notchpay", data
            )
        else:  # The customer cancelled the payment by clicking on the close button.
            pass  # Don't try to process this case because the transaction id was not provided.

        # Redirect the user to the status page.
        return request.redirect("/payment/status")

    @http.route(_auth_return_url, type="http", methods=["GET"], auth="public")
    def notchpay_return_from_authorization(self, response):
        """Process the response sent by Notchpay after authorization.
        """
        data = json.loads(response)
        return self.notchpay_return_from_checkout(**data)
