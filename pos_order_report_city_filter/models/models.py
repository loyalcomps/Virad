# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosOrderReport(models.Model):
    _inherit = "report.pos.order"

    city = fields.Char()

    def _select(self):
        return super(PosOrderReport, self)._select() + ',rp.city AS city'

    def _from(self):
        return super(PosOrderReport, self)._from() + ' LEFT JOIN res_partner rp on (s.partner_id=rp.id)'

    def _group_by(self):
        return super(PosOrderReport, self)._group_by() + ',rp.id'
