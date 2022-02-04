# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosConfig(models.Model):
    _inherit = 'pos.config'

    auto_invoice_check = fields.Boolean(string="Auto Invoice Check", help='Default invoice button is selected in pos.', default=False,
                                        )
    no_invoice_print = fields.Boolean(string="Invoice Print not Required", default=False)

    @api.onchange('module_account')
    def change_invoice_check_account(self):
        for record in self:
            if not record.module_account:
                record.auto_invoice_check = False
                record.no_invoice_print = False
