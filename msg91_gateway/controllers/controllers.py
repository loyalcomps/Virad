# -*- coding: utf-8 -*-
import logging
from odoo.http import request
from odoo import http, SUPERUSER_ID
from odoo.exceptions import Warning
import requests
import urllib
import json
import base64
from odoo import models, fields, api, _
_logger = logging.getLogger(__name__)
import ast


class MSG91Notify(http.Controller):
    @http.route(['/msg91/notification'], type='http', auth='public', website=True, csrf=False)
    def msg91_notification(self, **post):
        """ msg91 notification controller"""

        _logger.info(
            "LOYAL DEBUG FOR MSG91: SUMMARY(POST DATA)%r", post)
        all_sms_report = request.env["sms.report"].sudo().search(
            [('state', 'in', ('sent', 'new'))])
        for sms in all_sms_report:
            if sms.msg91_message_id and sms.msg91_api_key:
                sms_sms_obj = sms.sms_sms_id
                sms.status_hit_count += 1
                content = eval(post.get('data'))
                for data in content:
                    if data.get('requestId') == sms.msg91_message_id:
                        for report in data.get('report'):
                            number = str(sms.to).split(
                                '+')[1] if str(sms.to).startswith('+') else str(sms.to)
                            if str(report.get('number')) == number:
                                if report.get('status') == '16':
                                    sms.state = "new"
                                if report.get('status') == '1':
                                    if sms.auto_delete:
                                        sms.sudo().unlink()
                                        request._cr.commit()
                                        if sms_sms_obj.auto_delete and not sms_sms_obj.sms_report_ids:
                                            sms_sms_obj.sudo().unlink()
                                            request._cr.commit()
                                        break
                                    else:
                                        sms.state = "delivered"
                                        request._cr.commit()
                                if report.get('status') == '2':
                                    sms.state = "undelivered"
                                    request._cr.commit()
        return {}
