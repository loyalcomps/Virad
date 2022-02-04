# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _get_default_pos_location(self):
        return self.env['stock.warehouse'].search([('company_id', '=', self.env.user.company_id.id)],
                                                  limit=1).lot_stock_id

    pos_stock_location_id = fields.Many2one(
        'stock.location', string='POS Stock Location',
        domain=[('usage', '=', 'internal')], required=True, default=_get_default_pos_location)


class Warehouse(models.Model):
    _inherit = "stock.warehouse"

    def _get_partner_pos_location(self):
        return self.env['stock.warehouse'].search(
            [('company_id', '=', self.env.user.company_id.id)],
            limit=1).lot_stock_id


class PosOrder(models.Model):
    _inherit = "pos.order"

    def _create_order_picking(self):
        self.ensure_one()
        if not self.session_id.update_stock_at_closing or (self.company_id.anglo_saxon_accounting and self.to_invoice):
            picking_type = self.config_id.picking_type_id
            if self.partner_id.pos_stock_location_id:
                destination_id = self.partner_id.pos_stock_location_id.id
            elif not picking_type or not picking_type.default_location_dest_id:
                destination_id = self.env['stock.warehouse']._get_partner_pos_location().id
            else:
                destination_id = picking_type.default_location_dest_id.id

            pickings = self.env['stock.picking']._create_picking_from_pos_order_lines(destination_id, self.lines,
                                                                                      picking_type, self.partner_id)
            pickings.write({'pos_session_id': self.session_id.id, 'pos_order_id': self.id, 'origin': self.name})


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _create_picking_at_end_of_session(self):
        self.ensure_one()
        lines_grouped_by_dest_location = {}
        picking_type = self.config_id.picking_type_id

        if not picking_type or not picking_type.default_location_dest_id:
            session_destination_id = self.env['stock.warehouse']._get_partner_pos_location().id
        else:
            session_destination_id = picking_type.default_location_dest_id.id

        for order in self.order_ids:
            if order.company_id.anglo_saxon_accounting and order.to_invoice:
                continue
            destination_id = order.partner_id.pos_stock_location_id.id or session_destination_id
            if destination_id in lines_grouped_by_dest_location:
                lines_grouped_by_dest_location[destination_id] |= order.lines
            else:
                lines_grouped_by_dest_location[destination_id] = order.lines

        for location_dest_id, lines in lines_grouped_by_dest_location.items():
            pickings = self.env['stock.picking']._create_picking_from_pos_order_lines(location_dest_id, lines,
                                                                                      picking_type)
            pickings.write({'pos_session_id': self.id, 'origin': self.name})

