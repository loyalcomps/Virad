# -*- coding: utf-8 -*-


from odoo import models, fields, api, _
from odoo import SUPERUSER_ID
import re
import operator
from odoo.exceptions import except_orm, Warning, RedirectWarning


class SmsReport(models.Model):
    """SMS report for every mobile number of sms."""

    _name = "sms.report"
    _inherit = 'sms.base.abstract'
    _description = "Model for sms report."
    _order = "id desc"
    _rec_name = "to"

    state = fields.Selection([
        ('new', 'Outgoing'),
        ('sent', 'Sent'),
        ('delivered', 'Delivered'),
        ('error', 'error'),
        ('undelivered', 'Undelivered'),
    ], string="Status", default="new")
    sms_sms_id = fields.Many2one("sms.notification", string="SMS")
    auto_delete = fields.Boolean(related="sms_sms_id.auto_delete", string="Auto Delete",
                                 help="Permanently delete this SMS after sending it,to save space.")
    status_hit_count = fields.Integer(
        string="Total count of trial of getting status using cron.")

    @api.model
    def cron_function_for_sms(self):
        pass
