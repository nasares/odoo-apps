from odoo import fields, models


class Books(models.Model):
    _inherit = 'product.template'

    is_book = fields.Boolean(string="Is Book ?", default=False)
