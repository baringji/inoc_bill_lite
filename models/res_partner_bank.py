from odoo import api, fields, models


class ResPartnerBank(models.Model):
    _inherit = ["res.partner.bank"]

    bill_com_id = fields.Char(
        string="Bill.com ID",
        help="""Bill-generated ID of the bank accounts. The value begins with 
            bac: Company's bank account
            cba: Customer's bank account
            vba: Vendor's bank account""",
    )
    bill_com_id_synced_at = fields.Datetime(string="Synced At")
