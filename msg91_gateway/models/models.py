# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class msg91_gateway(models.Model):
#     _name = 'msg91_gateway.msg91_gateway'
#     _description = 'msg91_gateway.msg91_gateway'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
