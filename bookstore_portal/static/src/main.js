odoo.define('bookstore_portal/static/src/main.js', function(require){

'use strict';

const App = require('bookstore_portal/static/src/components/app.js');

const { QWeb, utils, Component } = owl;

async function start() {

  if (document.querySelector("#books")) {
      const [templates] = await Promise.all([
        utils.loadFile("bookstore_portal/static/src/components/templates.xml"),
        utils.whenReady()
      ]);
      const qweb = new QWeb({ templates });
      Component.env = { qweb };
      const app = new App();
      app.mount(document.querySelector("#books"));
  }

}

start();

})