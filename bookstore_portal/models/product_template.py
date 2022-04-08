from odoo import fields, models, api


class Books(models.Model):
    _inherit = 'product.template'

    pages_number = fields.Integer()
    url = fields.Char()
