from odoo import fields, models


class BookstoreCollection(models.Model):
    _name = 'bookstore.collection'
    _rec_name = 'name'

    name = fields.Char()
