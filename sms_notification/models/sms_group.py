# -*- coding: utf-8 -*-


from odoo import models, fields, api, _


class SmsGroup(models.Model):

    _name = "sms.group"
    _description = "This module is used for create the group of customer to send message"

    name = fields.Char(string="Group Name", required=True)
    member_type = fields.Selection([('customer', 'Customer'),
                                    ('supplier', 'Supplier'),
                                    ('any', 'Any')], string="Member Type", default="customer", required=True)
    member_ids = fields.Many2many("res.partner", 'sms_member_group',
                                  column1='member_id', column2='partner_id', string="Members", required=True)
    total_members = fields.Integer(
        compute='get_total_members', string="Total Members", store=True)

    @api.depends("member_ids")
    def get_total_members(self):
        for i in self:
            i.total_members = len(i.member_ids)

