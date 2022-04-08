odoo.define('bookstore_portal/static/src/components/list/list.js', function(require) {

'use strict';

const { Component } = owl;
const { useState } = owl.hooks;
const components = {
    Search: require('bookstore_portal/static/src/components/search/search.js'),
};

class List extends Component {

    constructor(parent, props) {
        super(parent, props);
        this.state = useState({"books": []});
        this.getBooks()
    }

    handleBooks(result) {
        for (let res of result) {
            this.state["books"].push({
                "title":res.title,
                "price":res.price,
                "pages_number":res.pages_number,
                "kind":res.kind,
            })
        }
    }

    async getBooks() {
        let result;
        await owl.browser.fetch('/books/list/data')
        .then(response => response.json())
        .then(function(data) {
            result = data.result
        })
        .catch(function(error) {
            console.log(error);
        });
        this.handleBooks(result)
    }

    get listBooks() {
        return this.state.books
    }

}

Object.assign(List, {
    defaultProps: {
        class: 'book-list'
    },
    Props: {
        search: {
            type: Boolean,
            element: Boolean,
            optional: true
        },
        columns: {
            type: Array,
            element: String,
            optional: false
        },
        values: {
            type: Array,
            element: String,
            optional: false
        },
    },
    components,
    template: 'bookstore_portal.List'
});

return List;

})
