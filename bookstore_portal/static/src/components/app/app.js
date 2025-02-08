/** @odoo-module **/

import { Component } from "@odoo/owl";
import { List } from "@bookstore_portal/components/list/list";

export class App extends Component {
  static template = 'bookstore_portal.App';
  static components = { List }; 
  
  setup() {
    this.columns = ['Title', 'Price', 'Pages', 'Kind'];
  }

}

