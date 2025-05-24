from odoo import models, fields, api


class StockPackageTypeInherit(models.Model):
    _inherit = 'stock.package.type'

    product_id = fields.Many2one(
        'product.product',
        string='Product',
        help='Product linked to this package type'
    )
