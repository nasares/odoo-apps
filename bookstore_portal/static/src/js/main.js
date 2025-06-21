/** @odoo-module **/

import { mount } from "@odoo/owl";
import { templates } from "@web/core/assets";
import { App } from "@bookstore_portal/components/app/app";

owl.whenReady( () => {
    const target = document.querySelector("#app") || document.body;
    mount(App, target, { templates, dev: false });
});

