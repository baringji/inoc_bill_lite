from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = ["account.move"]

    bill_com_id = fields.Char(
        string="Bill.com ID",
        help="""Bill-generated ID of the transactions. The value begins with 
            00e: Invoices
            00n: Bills""",
    )
    bill_com_id_synced_at = fields.Datetime(string="Synced At")
