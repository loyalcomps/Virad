# -*- coding: utf-8 -*-
# from odoo import http


# class SmsNotification(http.Controller):
#     @http.route('/sms_notification/sms_notification/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sms_notification/sms_notification/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sms_notification.listing', {
#             'root': '/sms_notification/sms_notification',
#             'objects': http.request.env['sms_notification.sms_notification'].search([]),
#         })

#     @http.route('/sms_notification/sms_notification/objects/<model("sms_notification.sms_notification"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sms_notification.object', {
#             'object': obj
#         })
