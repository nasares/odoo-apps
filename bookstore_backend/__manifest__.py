{
    'name': 'Bookstore Backend',
    "summary": "Odoo module for library management",
    'category': 'Sales',
    "images": ['static/description/images/undraw_books_6rhq.png'],
    'version': '14.0.1.0.0',
    "author": "Nasser",
    "website": "https://nasser.cm/",
    "license": "LGPL-3",
    'depends': ['base', 'sale_management', 'purchase', 'stock'],
    'data': [
        'data/menu.xml',
        'security/ir.model.access.csv',
        'views/product_template.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
