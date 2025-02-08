{
    'name': "Bookstore Portal",
    'summary': """Customers can get books throughout the portal""",
    'category': 'Sales',
    "images": ['static/description/images/undraw_books_6rhq.png'],
    'version': '16.0.1.0.0',
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
            # CSS style
            'bookstore_portal/static/src/css/style.css',

            # Load XML first
            'bookstore_portal/static/src/components/search/search.xml',
            'bookstore_portal/static/src/components/list/list.xml',
            'bookstore_portal/static/src/components/app/app.xml',

            # Then load JS
            'bookstore_portal/static/src/components/search/search.js',
            'bookstore_portal/static/src/components/list/list.js',
            'bookstore_portal/static/src/components/app/app.js',

            # The main JS at the end
            'bookstore_portal/static/src/js/main.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}

