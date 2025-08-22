{
    "name": "Contact Rating",
    "version": "17.0.1.0.0",
    "summary": "Contact notation system with stars",
    "description": """
        This module extends the existing Contacts module to add
        a star rating system (1-5) to mesure quality of the relationship 
        with a contact
    """,
    "author": "Peef",
    "website": "https://peef.dev/",
    "license": "LGPL-3",
    "sequence": "-1",
    "depends": [
        "base",
        "contacts"
    ],
    "data": [
        "views/res_partner_views.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
