# -*- coding: utf-8 -*-

from functools import partial

from odoo import models, fields


class PosOrderReport(models.Model):
    _inherit = "report.pos.order"

    muncipality_id = fields.Many2one('muncipality.name', string="Local Body Name",readonly=True)


    def _select(self):
        return super(PosOrderReport, self)._select() + ',s.muncipality_id AS muncipality_id'

    def _group_by(self):
        return super(PosOrderReport, self)._group_by() + ',s.muncipality_id'
