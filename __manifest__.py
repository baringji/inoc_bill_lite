{
    "name": "Bill Connect API Integration",
    "summary": """
        Bill.com V3 REST API integration.
    """,
    "description": """
        Features:
        - Bill.com V3 REST API connection.
        - Create a vendor and bill.
        - Syncing vendor, bill and bank account.
        - Create a customer and invoice.
        - Syncing customer, invoice and bank account.
    """,
    "author": "inoc IT Solutions",
    "website": "https://inoc.me",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "17.0.0.0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "account"],
    # always loaded
    "data": [
        # "data/res_partner_cron.xml",
        # "security/ir.model.access.csv",
        "views/account_move_views.xml",
        "views/res_company_views.xml",
        "views/res_partner_views.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
