{
    'name': "Delivery Package",
    'summary': """Optimizing delivery packaging""",
    'sequence': '-110',
    'category': 'stock',
    'version': '18.0.1.0.0',
    "author": "Nasser",
    "license": "LGPL-3",
    'depends': [
        # standard
        'base',
        'stock',
        'stock_delivery',

        # Third party
        'product_dimension'

    ],
    'data': [
        # data
        "data/base_data.xml",

        # views
        "views/stock_package_type_views.xml",
        "views/stock_picking_views.xml",
        "views/stock_quant_package_views.xml",
    ],
    'assets': {},
    'installable': True,
    'application': True,
    'auto_install': False,
}

