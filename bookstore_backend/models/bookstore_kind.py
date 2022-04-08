from odoo import fields, models


class BookstoreKind(models.Model):
    _name = 'bookstore.kind'
    _rec_name = 'name'

    name = fields.Char()
