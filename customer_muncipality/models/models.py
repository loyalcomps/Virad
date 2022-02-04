# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError, ValidationError


class Muncipality_Name(models.Model):
    _name = 'muncipality.name'
    _description = 'Local Body'

    name = fields.Char(string="Local Body Name")

class ResPartner(models.Model):
    _inherit = "res.partner"

    muncipality_id = fields.Many2one('muncipality.name',string="Local Body Name")


class PosOrder(models.Model):
    _inherit = 'pos.order'

    muncipality_id = fields.Many2one('muncipality.name', string="Local Body Name",related='partner_id.muncipality_id',store=True)



