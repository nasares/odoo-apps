{
    'name': "Bookstore Portal",
    'summary': """Customers can get books throughout the portal""",
    'category': 'Sales',
    "images": ['static/description/images/undraw_books_6rhq.png'],
    'version': '15.0.1.0.0',
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
        'views/index.xml',
        'views/product_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'bookstore_portal/static/src/css/style.css',
            'bookstore_portal/static/src/components/list/list.js',
            'bookstore_portal/static/src/components/search/search.js',
            'bookstore_portal/static/src/components/app.js',
            'bookstore_portal/static/src/main.js'
        ],
        'web.assets_qweb': [
            'bookstore_portal/static/src/components/templates.xml',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
