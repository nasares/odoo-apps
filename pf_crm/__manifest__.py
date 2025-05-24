{
    'name': 'Peef Odoo',
    'category': 'Peef',
    'description': 'Odoo customisation for Peef management, not website',
    'version': '18.0.0.0.0',
    'author': 'Nasser',
    'website': 'https://www.peef.dev',
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': -100,
    'depends': [
        'base',
        'crm',
    ],
    'data': [
        "views/res_partner_views.xml",
    ],
}
