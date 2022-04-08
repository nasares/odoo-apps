from odoo import http
import json


class BookstoreController(http.Controller):

    def get_books_list(self):
        books = http.request.env['product.template'].sudo().search([])
        list_books = []
        for book in books:
            list_books.append({
                'title': book.name,
                'price': book.list_price,
                'pages_number': book.pages_number,
                'kind': book.kind_id.name,
            })
        return list_books

    def get_books_result(self):
        return {'result': self.get_books_list()}

    @http.route('/books', auth='public', website=True)
    def index(self):
        values = {'data': self.get_books_list()}
        return http.request.render('bookstore_portal.index', values)

    @http.route('/books/list/data', auth='public', type='http')
    def book_list_json(self):
        """ Get books data in a JSON format """
        values = self.get_books_result()
        return json.dumps(values)

    @http.route('/books/search/', auth='public', type='http')
    def book_search(self):
        values = self.get_books_result()
        return json.dumps(values)
