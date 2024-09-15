from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = ["res.partner"]

    bill_com_id = fields.Char(
        string="Bill.com ID",
        help="""Bill-generated ID of the organizations. The value begins with 
            008: Companies
            009: Vendors
            0cu: Customers""",
    )
    bill_com_id_synced_at = fields.Datetime(string="Synced At")
