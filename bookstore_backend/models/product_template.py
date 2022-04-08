from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    author_id = fields.Many2one(
        comodel_name='res.partner',
        string='Author'
    )
    kind_id = fields.Many2one(
        comodel_name='bookstore.kind',
        string='Kind'
    )
    editor_id = fields.Many2one(
        comodel_name='res.partner',
        string='Editor'
    )
    collection_id = fields.Many2one(
        comodel_name='bookstore.collection',
        string='Collection'
    )
    resume = fields.Text(string="Resume")
    isbn_code = fields.Char(string='ISBN Code')
