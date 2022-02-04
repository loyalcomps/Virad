# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.tools.safe_eval import safe_eval


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    def _check_twilio(self):
        result = self.env['ir.module.module'].search(
            [('name', '=', 'twilio_gateway')])
        if result:
            return True
        else:
            return False

    def _check_plivo(self):
        result = self.env['ir.module.module'].search(
            [('name', '=', 'plivo_gateway')])
        if result:
            return True
        else:
            return False

    def _check_clicksend(self):
        result = self.env['ir.module.module'].search(
            [('name', '=', 'clicksend_gateway')])
        if result:
            return True
        else:
            return False

    def _check_msg91(self):
        result = self.env['ir.module.module'].search(
            [('name', '=', 'msg91_gateway')])
        if result:
            return True
        else:
            return False

    def _check_mobily(self):
        result = self.env['ir.module.module'].search(
            [('name', '=', 'mobily_gateway')])
        if result:
            return True
        else:
            return False

    def _check_skebby(self):
        result = self.env['ir.module.module'].search(
        [('name', '=', 'skebby_gateway')])
        if result:
            return True
        else:
            return False

    module_twilio_gateway = fields.Boolean(
        string='Install Twilio SMS Gateway', help='It will Install twilio sms gateway automatically.')
    is_twilio_in_addon = fields.Boolean(default=_check_twilio)

    module_plivo_gateway = fields.Boolean(
        string='Install Plivo SMS Gateway', help='It will Install plivo sms gateway automatically.')
    is_plivo_in_addon = fields.Boolean(default=_check_plivo)

    module_clicksend_gateway = fields.Boolean(
        string='Install Clicksend SMS Gateway', help='It will Install clicksend sms gateway automatically.')
    is_clicksend_in_addon = fields.Boolean(default=_check_clicksend)

    module_msg91_gateway = fields.Boolean(
        string='Install MSG91 SMS Gateway', help='It will Install MSG91 sms gateway automatically.')
    is_msg91_in_addon = fields.Boolean(default=_check_msg91)

    module_mobily_gateway = fields.Boolean(
        string='Install Mobily SMS Gateway', help='It will Install MSG91 sms gateway automatically.', default=False)
    is_mobily_in_addon = fields.Boolean(default=_check_mobily)

    module_skebby_gateway = fields.Boolean(
        string='Install Skebby SMS Gateway', help='It will Install Skebby sms gateway automatically.', default=False)
    is_skebby_in_addon = fields.Boolean(default=_check_skebby)

    is_phone_code_enable = fields.Boolean(string="Are you managing country calling code with customer's mobile number ?",
                                          help="If not enabled then it will pick country calling code from the country selected in customer. In case customer has no country then it will pick country calling code from company's country.")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        res.update(
            is_phone_code_enable=params.get_param('sms_notification.is_phone_code_enable', default=False),
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.ensure_one()
        self.env['ir.config_parameter'].sudo().set_param('sms_notification.is_phone_code_enable', repr(self.is_phone_code_enable))
