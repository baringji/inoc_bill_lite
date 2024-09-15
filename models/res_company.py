from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = ["res.company"]

    bill_username = fields.Char(
        string="Username", help="Your username is the email address used to sign in to your BILL developer account."
    )
    bill_password = fields.Char(
        string="Password",
        help="Your password is used to sign in to your BILL developer account.",
    )
    bill_organization_id = fields.Char(
        string="Organization ID",
        help="Your BILL developer account represents your organization in BILL. The organization id is unique alphanumeric value that begins with 008.",
    )
    bill_developer_key = fields.Char(
        string="Developer Key",
        help="Your developer key is used to identify your developer account in your API requests.",
    )
    is_sandbox = fields.Boolean(default=True)
    base_url = fields.Char(
        help="Production API base URL.",
        default="https://gateway.prod.bill.com/connect/v3",
    )
    sandbox_base_url = fields.Char(
        help="Sandbox API base URL.",
        default="https://gateway.stage.bill.com/connect/v3",
    )
