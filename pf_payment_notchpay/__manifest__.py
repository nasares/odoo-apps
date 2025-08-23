{
    "name": "Payment Notchpay",
    "summary": "Orange Money and MTN Mobile Money payment integration with Notchpay provider for Cameroon",
    "description": "",  # empty to avoid loading the readme file
    "sequence": "-110",
    "category": "Accounting/Payment Providers",
    "version": "18.0.1.0.0",
    "author": "Nasser",
    "website": "https://www.peef.dev",
    "license": "LGPL-3",
    "depends": [
        # standard
        "base",
        "payment",
    ],
    "data": [
        # views
        "views/payment_notchpay_templates.xml",
        "views/payment_provider_views.xml",
        "views/payment_transaction_views.xml",
        # data
        "data/payment_provider_data.xml",
    ],
    "assets": {},
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
    "installable": True,
    "application": True,
    "auto_install": False,
}
