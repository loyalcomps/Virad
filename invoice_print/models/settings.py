from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    account_note = fields.Char(string="Invoice Terms and Conditions")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        res.update(
            account_note=params.get_param('invoice_print.account_note') or False,
        )
        return res

    def set_values(self):
        self.ensure_one()
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param("invoice_print.account_note", self.account_note)


