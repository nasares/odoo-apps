// HOW TO IMPLEMENT A SEARCH FUNCTIONNALITY
// 1. Create a controller /search/<element to search> in python side
// 2. Trigger an action in JS side when we press <KEY ENTER> to call the controller
// 3. Filter the table in JS side based on the response we have
// Tutorial: https://www.youtube.com/watch?v=wxz5vJ1BWrc

odoo.define('bookstore_portal/static/src/components/search/search.js', function(require){

'use strict';

const { Component } = owl;
const { useState } = owl.hooks;

class Search extends Component {

    constructor(parent, props) {
        super(parent, props);
    }

    async doSearch(ev) {
        const searchInput = document.getElementById('do-Search')
        if (ev.keyCode === 13) {
            try {
                await owl.browser.fetch("/books/search/")
                    .then(response => response.json())
                    .then(response => {
                        const filteredResult = response.result.filter(function (input) {
                            return input.title.includes(searchInput.value);
                        });
                        this.displayFiltered(filteredResult)
                    });
            } catch (error) {
                console.error(error);
            }
        }

    }

    displayFiltered(elements) {
        const newContent = elements.map((element) => {
            return `
                <table id="book-list-filtered">
                    <tr>
                        <th>Title</th>
                        <th>Price</th>
                        <th>Pages</th>
                        <th>Kind</th>
                    </tr>
                    <tr>
                        <td>${element.title}</td>
                        <td>${element.price}</td>
                        <td>${element.pages_number}</td>
                        <td>${element.kind}</td>
                    </tr>
                </table>
                `
        })
        document.getElementById("book-list-all").innerHTML = newContent[0]
    }

}

Object.assign(Search, {
    defaultProps: {
        class: 'search-box'
    },
    template: 'bookstore_portal.Search'
});

return Search;

})
