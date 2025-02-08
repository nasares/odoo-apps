/** @odoo-module */

// HOW TO IMPLEMENT A SEARCH FUNCTIONNALITY
// 1. Create a controller /search/<element to search> in python side
// 2. Trigger an action in JS side when we press <KEY ENTER> to call the controller
// 3. Filter the table in JS side based on the response we have
// Tutorial: https://www.youtube.com/watch?v=wxz5vJ1BWrc

import { Component } from "@odoo/owl";
import { useRef } from "@odoo/owl";

export class Search extends Component {
  static template = 'bookstore_portal.Search';
  
  setup() {
    this.searchInput = useRef("searchInput");
  }

  async doSearch(ev) {
      if (ev.keyCode === 13) {
          try {
            const response = await fetch("/books/search/");
            const data = await response.json();
            const searchTerm = this.searchInput.el.value.toLowerCase();
            const filteredResult = data.result.filter((input) =>
	              input.title.toLowerCase().includes(searchTerm)
            );
            this.displayFiltered(filteredResult);
          } catch (error) {
            console.error(error);
          }
      }
  }

  displayFiltered(elements) {
    if (!elements.length) {
      document.getElementById("book-list-all").innerHTML = `
          <div class="alert alert-warning" role="alert">
              No result found
          </div>
      `;
      return;
    }

    const tableContent = elements.map((element) => `
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
    `);
    document.getElementById("book-list-all").innerHTML = tableContent[0];
  }
}


Search.props = {
    class: { type: String, optional: true, default: 'search-box' }
};

