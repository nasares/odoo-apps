/** @odoo-module **/

import { mount } from "@odoo/owl";
import { templates } from "@web/core/assets";
import { App } from "@bookstore_portal/components/app/app";

owl.whenReady( () => {
    mount(App, document.getElementById("app"), { templates, dev: false });
});

