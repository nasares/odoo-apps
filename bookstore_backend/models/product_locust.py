"""
These functions are used for the HappyToShare webinar related to Odoo Performance Optimisation
The locust scripts are available in the locust folder of this repository
The YouTube video is available at : https://youtu.be/AcCbjeasAyY

Peef is a marketplace that connect developers and entreprises at https://peef.dev

Peef, Unlock you potential
"""

from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def count_books_by_collection_np(self):
        # Get all collections
        collections = self.env['bookstore.collection'].search([])
        result = {}

        # Perform individual count queries (inefficient)
        for collection in collections:
            domain = [('collection_id', '=', collection.id)]
            book_count = self.search_count(domain)
            if book_count > 0:
                result[collection.id] = {
                    'collection_name': collection.name,
                    'book_count': book_count
                }

        return result

    @api.model
    def count_books_by_collection(self):
        # Get all collections first
        collections = self.env['bookstore.collection'].search([])
        collection_ids = collections.ids

        if not collection_ids:
            return {}

        # Using read_group to get all counts in a single query
        domain = [('collection_id', 'in', collection_ids)]
        counts_data = self.read_group(
            domain=domain,
            fields=['collection_id'],
            groupby=['collection_id']
        )

        # Convert to dictionary for easy lookup
        mapped_data = {}
        for item in counts_data:
            collection_id = item['collection_id'][0] if item.get('collection_id') else False
            if collection_id:
                mapped_data[collection_id] = item['collection_id_count']

    @api.model
    def show_all_books_name_of_test_collection_3_np(self):
        collection = self.env["bookstore.collection"].search([("name", "=", "Test Collection 3")])
        books = self.search([("collection_id", "=", collection.id)])
        return books.mapped("name")

    @api.model
    def show_all_books_name_of_test_collection_3_browse(self):
        collection = self.env["bookstore.collection"].browse(10)
        books = self.search_read([("collection_id", "=", collection.id)], ["name"])
        return books

    @api.model
    def show_all_books_name_of_test_collection_3(self):
        collections = self.env["bookstore.collection"].search_read(
            domain=[("name", "=", "Test Collection 3")],
            fields=["id"],
            limit=1
        )

        if not collections:
            return []

        collection_id = collections[0]["id"]

        books = self.search_read(
            domain=[("collection_id", "=", collection_id)],
            fields=["name"]
        )

        return [book["name"] for book in books]
