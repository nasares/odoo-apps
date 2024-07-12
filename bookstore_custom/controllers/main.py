from odoo import http
from ...bookstore_portal.controllers.main import BookstoreController

class BookstoreControllerInherit(BookstoreController):

    def get_books_list(self):
        list_books = []
        books = http.request.env['product.template'].sudo().search([('is_book','=',True)])
        for book in books:
            list_books.append({
                'title': book.name,
                'price': book.list_price,
                'pages_number': book.pages_number,
                'kind': book.kind_id.name,
            })
        return list_books
    
    
    
