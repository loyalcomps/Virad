# -*- coding: utf-8 -*-


from odoo import models, fields, api, _
import re
from functools import reduce
import operator
from odoo import tools, api


from html.parser import HTMLParser

import logging
_logger = logging.getLogger(__name__)


# http://stackoverflow.com/questions/38200739/extract-text-from-html-mail-odoo
class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


class SmsNotificationTemplate(models.Model):
    "Templates for sending sms"
    _name = "sms.notification.template"
    _description = 'SMS Notification Templates'
    _order = 'name'

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char('Name', required=True)
    auto_delete = fields.Boolean("Auto Delete")
    globally_access = fields.Boolean(
        string="Global", help="if enable then it will consider normal(global) template.You can use it while sending the bulk message. If not enable the you have to select condition on which the template applies.")
    condition = fields.Selection([('order_placed', 'Order Placed'),
                                  ('order_confirm', 'Order Confirmed'),
                                  ('order_delivered', 'Order Delivered'),
                                  ('invoice_vaildate', 'Invoice Validate'),
                                  ('invoice_paid', 'Invoice Paid'),
                                  ('order_cancel', 'Order Cancelled')], string="Conditions", help="Condition on which the template has been applied.")
    model_id = fields.Many2one(
        'ir.model', 'Applies to', compute="onchange_condition", help="The kind of document with this template can be used. Note if not selected then it will consider normal(global) template.", store=True)
    model = fields.Char(related="model_id.model", string='Related Document Model',
                        store=True, readonly=True)
    sms_body_html = fields.Text('Body', translate=True, sanitize=False,
                                help="SMS text. You can also use ${object.partner_id} for dynamic text. Here partner_id is a field of the document(obj/model).", )

    dlt_te_id = fields.Char(string='DLT TE ID')

    @api.model
    def _get_default_config_sms_gateway(self):
        return self.env["sms.mail.server"].search([], order='sequence asc', limit=1)

    sms_gateway_config_id = fields.Many2one(
        'sms.mail.server', string="SMS Gateway", default=_get_default_config_sms_gateway)
    to = fields.Char("To:", )
    group_ids = fields.Many2one("sms.group", string="Group")
    # @api.onchange('globally_access')
    # def onchange_globally_access(self):
    #     if self.globally_access:
    #         self.condition = False

    def _get_partner_mobile(self, partner):
        mobile = partner.mobile if partner.mobile else partner.phone
        mobile = mobile if mobile is not False else ""
        mobile = str(mobile).replace(" ", "")
        if not mobile:
            return ""
        company_country_calling_code = self.env.user.company_id.country_id.phone_code
        managed_calling_code = self.env['ir.config_parameter'].get_param(
            'sms_notification.is_phone_code_enable', 'False') == 'True'
        if managed_calling_code:
            if len(str(mobile)) == 10:
                mobile_no = "+{code}{mobile}".format(code=company_country_calling_code, mobile=mobile)
            elif len(str(mobile)) >= 13:
                mobile_no = "{mobile}".format(mobile=mobile)
            else:
                mobile_no = "+{code}{mobile}".format(code=company_country_calling_code, mobile=mobile)
            return mobile_no
        if partner.country_id and partner.country_id.phone_code:
            country_calling_code = partner.country_id.phone_code
        else:
            country_calling_code = company_country_calling_code
        if len(str(mobile)) == 10:
            mob = "+{code}{mobile}".format(code=country_calling_code, mobile=mobile)
        elif len(str(mobile)) >= 13:
            mob = "{mobile}".format(mobile=mobile)
        else:
            mob = "+{code}{mobile}".format(code=country_calling_code, mobile=mobile)
        return mob

    def _get_partner_mobile_numbers(self, group):
        return [self._get_partner_mobile(partner) for partner in group.member_ids if partner.mobile or partner.phone]

    @api.onchange('group_ids')
    def add_group_member_number(self):
        phone_lists = [self._get_partner_mobile_numbers(
            group) for group in self.group_ids if self.group_ids]
        combined_list = reduce(
            operator.add, phone_lists) if phone_lists else []
        self.to = self.get_mobile_number(list(set(combined_list)))

    @api.model
    def get_mobile_number(self, mob_no):
        # Here mob_no is a list of str of mobile number we are using msg91 so
        if self.sms_gateway_config_id.gateway == "plivo":
            return '<'.join(mob_no)
        elif self.sms_gateway_config_id.gateway == "clicksend":
            return ','.join(mob_no)
        else:
            return ','.join(mob_no)

    @api.onchange('globally_access')
    def onchange_globally_access(self):
        if self.globally_access:
            self.condition = False

    @api.depends('condition')
    def onchange_condition(self):
        for i in self:
            if i.condition:
                if i.condition in ['order_placed', 'order_confirm', 'order_cancel']:
                    model_id = self.env['ir.model'].search(
                        [('model', '=', 'sale.order')])
                    i.model_id = model_id.id if model_id else False
                elif i.condition in ['order_delivered']:
                    model_id = self.env['ir.model'].search(
                        [('model', '=', 'stock.picking')])
                    i.model_id = model_id.id if model_id else False
                elif i.condition in ['invoice_vaildate', 'invoice_paid']:
                    model_id = self.env['ir.model'].search(
                        [('model', '=', 'account.move')])
                    i.model_id = model_id.id if model_id else False
            else:
                i.model_id = False

    @api.onchange('model_id')
    def onchange_model_id(self):
        for i in self:
            if i.model_id:
                i.model = i.model_id.model
            else:
                i.model = False

    def get_body_data(self, obj):
        self.ensure_one()
        if obj:
            if 'partner_id' in obj:
                lang = obj.partner_id.lang
            else:
                lang = obj.user_id.lang
            body_msg = self.env["mail.template"].with_context(lang=lang).sudo()._render_template(
                self.sms_body_html, self.model, [obj.id])
            new_body_msg = re.sub("<.*?>", " ", body_msg[obj.id])
            return new_body_msg
            return " ".join(strip_tags(new_body_msg).split())

    @api.model
    def send_sms_using_template(self, mob_no, sms_tmpl, sms_gateway=None, obj=None):
        if not sms_gateway:
            gateway_id = self.env["sms.mail.server"].search(
                [], order='sequence asc', limit=1)
        else:
            gateway_id = sms_gateway
        if mob_no and sms_tmpl and obj:
            sms_sms_obj = self.env["sms.notification"].create({
                'sms_gateway_config_id': gateway_id.id,
                'partner_id': obj.partner_id.id if 'partner_id' in obj else obj.user_id.partner_id.id,
                'to': mob_no,
                'group_type': 'individual',
                'auto_delete': sms_tmpl.auto_delete,
                'msg': sms_tmpl.get_body_data(obj),
                'template_id': False
            })
            sms_sms_obj.send_sms_via_gateway(
                sms_sms_obj.msg, [sms_sms_obj.to], from_mob=None, sms_gateway=gateway_id, sms_template=sms_tmpl)
