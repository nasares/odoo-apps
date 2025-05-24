from odoo import models, fields, api


class StockQuantPackageInherit(models.Model):
    _inherit = 'stock.quant.package'

    product_id = fields.Many2one(
        'product.product',
        string='Product',
        help='Product linked to this package'
    )