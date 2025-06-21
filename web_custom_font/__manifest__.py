{
    'name': 'Web custom font',
    "description": "Adding custom font in PDF reports",
    'category': 'Technical',
    'version': '17.0.1.0.0',
    "author": "Peef",
    "website": "https://peef.dev/",
    "license": "LGPL-3",
    "sequence": "-1",
    'depends': [
        'web',
        'l10n_din5008',
    ],
    'data': [
        'report/din5008_report_extended.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            (
                'after',
                'web/static/fonts/fonts.scss',
                'web_custom_font/static/fonts/fonts.scss',
            ),
        ]
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
