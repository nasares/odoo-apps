{
    'name': "Bookstore Custom",
    'category': 'Sales',
    'version': '14.0.1.0.0',
    "author": "Saly",
    "license": "LGPL-3",
    'depends': [
        'bookstore_portal',
    ],
    'data': [
        'security/sale_group_bookstore.xml',
        'security/ir.model.access.csv',
        'views/product_template.xml',
        # 'views/menus.xml',
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}