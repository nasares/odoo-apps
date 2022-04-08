{
    'name': "Bookstore Portal",
    'summary': """Customers can get books throughout the portal""",
    'category': 'Sales',
    "images": ['static/description/images/undraw_books_6rhq.png'],
    'version': '14.0.1.0.0',
    "author": "Nasser",
    "website": "https://nasser.cm/",
    "license": "LGPL-3",
    'depends': [
        'base',
        'portal',
        'website',
        'website_sale',
        'bookstore_backend',
    ],
    'data': [
        'views/assets.xml',
        'views/index.xml',
        'views/product_template.xml',
    ],
    'qweb': [
        'static/src/components/templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
