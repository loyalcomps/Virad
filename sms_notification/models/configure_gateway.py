# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SmsMailServer(models.Model):
    """This class is design for configuring the sms mail server."""

    _name = "sms.mail.server"
    _description = "Module for sms mail server configuration."
    _rec_name = 'description'

    @api.model
    def get_reference_type(self):
        return []

    description = fields.Char(string="Description", required=True)
    sequence = fields.Integer(
        string='Priority', help="Default Priority will be 0.")
    sms_debug = fields.Boolean(
        string="Debugging", help="If enabled, the error message of sms gateway will be written to the log file")
    user_mobile_no = fields.Char(
        string="Mobile No.", help="Ten digit mobile number with country code(e.g +91)")
    gateway = fields.Selection('get_reference_type', string="SMS Gateway")

