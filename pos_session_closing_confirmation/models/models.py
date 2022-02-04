# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pos_order(models.Model):
    _inherit = 'pos.order'

    total_pos_quantity = fields.Float(string='Total Quantities', compute='_total_pos_product_qty',
                                             help="Total Quantity",store=True)

    @api.depends('lines.qty')
    def _total_pos_product_qty(self):
        for record in self:
            total_qty = 0
            for line in record.lines:
                total_qty = total_qty + line.qty
            record.total_pos_quantity = total_qty
