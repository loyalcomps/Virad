# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions,  _


class PosOrder(models.Model):
    _inherit = 'pos.order'

    require_customer = fields.Selection(
        related='session_id.config_id.require_customer',
    )

    @api.constrains('partner_id', 'session_id')
    def _check_partner(self):
        for rec in self:
            if rec.require_customer != 'no' and not rec.partner_id:
                raise exceptions.ValidationError(_(
                    'Customer is required for this order and is missing.'))
