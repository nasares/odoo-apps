/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { Search } from "@bookstore_portal/components/search/search";

export class List extends Component {
  static template = 'bookstore_portal.List';
  static components = { Search };
  
  setup() {
    this.state = useState({ books: [] });
    this.getBooks();
  }

    async getBooks() {
        try {
            const response = await fetch('/books/list/data');
            const data = await response.json();
            if (data && data.result) {
                this.state.books = data.result;
            }
        } catch (error) {
            console.error('Error fetching books:', error);
        }
    }

    get listBooks() {
        return this.state.books;
    }
}

List.props = {
    class: { type: String, optional: true, default: 'book-list' },
    search: { type: Boolean, optional: true },
    columns: { type: Array, element: String },
};

