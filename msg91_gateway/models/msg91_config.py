# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import except_orm, Warning, RedirectWarning
from .msg91_messaging import send_sms_using_msg91

import logging
_logger = logging.getLogger(__name__)


class SmsMailServer(models.Model):
    """Configure the msg91 sms gateway."""

    _inherit = "sms.mail.server"
    _name = "sms.mail.server"
    _description = "MSG91 Gateway"

    msg91_api_key = fields.Char(string="Msg91 Api key")

    def test_conn_msg91(self):
        sms_body = "Msg91 Test Connection Successful........"
        mobile_number = self.user_mobile_no
        response = send_sms_using_msg91(
            sms_body, mobile_number, sms_gateway=self, sms_template=None)
        if response.get("type") == "success":
            if self.sms_debug:
                _logger.info(
                    "===========Test Connection status has been sent on %r mobile number", mobile_number)
            raise Warning(
                "Test Connection status has been sent on %s mobile number" % mobile_number)

        if response.get("type") == "error":
            if self.sms_debug:
                _logger.error(
                    "==========One of the information given by you is wrong. It may be [Mobile Number] or [Api key]")
            raise Warning(
                "One of the information given by you is wrong. It may be [Mobile Number] or [Api key]")

    @api.model
    def get_reference_type(self):
        selection = super(SmsMailServer, self).get_reference_type()
        selection.append(('msg91', 'MSG91'))
        return selection
