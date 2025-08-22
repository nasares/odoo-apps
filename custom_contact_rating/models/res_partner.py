from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    customer_rating = fields.Selection(
        [
            ("1", "⭐ (1/5) - Hard relation"),
            ("2", "⭐⭐ (2/5) - Correct relation"),
            ("3", "⭐⭐⭐ (3/5) - Good relation"),
            ("4", "⭐⭐⭐⭐ (4/5) - Very good relation"),
            ("5", "⭐⭐⭐⭐⭐ (5/5) - Excellent relation"),
        ],
        string="Client rating",
        default="3",
        help="Evaluate the quality of your relationship with this contact",
    )

    rating_notes = fields.Text(
        string="Rating comments",
        help="Add details about this rating",
    )

    @api.onchange("customer_rating")
    def _onchange_customer_rating(self):
        if self.customer_rating == "1":
            return {
                "warning": {
                    "title": "Warning",
                    "message": "This customer requires special follow-up",
                }
            }
        elif self.customer_rating == "5":
            return {
                "warning": {
                    "title": "Excellent !",
                    "message": "This customer is an excelent",
                }
            }
