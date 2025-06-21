{
    'name': 'Bookstore Backend',
    "description": "Odoo module for library management",
    'category': 'Sales',
    'version': '17.0.1.0.0',
    "author": "Peef",
    "website": "https://peef.dev/",
    "license": "OPL-1",
    "sequence": "-1",
    'depends': [
        'base',
        'sale_management',
        'purchase',
        'stock'
    ],
    'data': [
        # data
        # security
        'security/ir.model.access.csv',
        # views
        'views/product_template.xml',
        # menus
        'views/bookstore_backend_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
