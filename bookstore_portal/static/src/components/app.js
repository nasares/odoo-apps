odoo.define('bookstore_portal/static/src/components/app.js', function(require) {

'use strict';

const components = {
    List: require('bookstore_portal/static/src/components/list/list.js'),
};


const { Component } = owl;
const { useState } = owl.hooks;

class App extends Component {

    constructor() {
        super(...arguments);
        this.state = {books: new components.List().listBooks}
    }
}

Object.assign(App, {
    components,
    template: 'bookstore_portal.App',
});

return App;

})
