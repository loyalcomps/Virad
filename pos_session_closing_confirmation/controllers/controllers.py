# -*- coding: utf-8 -*-
# from odoo import http


# class PosSessionClosingConfirmation(http.Controller):
#     @http.route('/pos_session_closing_confirmation/pos_session_closing_confirmation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_session_closing_confirmation/pos_session_closing_confirmation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_session_closing_confirmation.listing', {
#             'root': '/pos_session_closing_confirmation/pos_session_closing_confirmation',
#             'objects': http.request.env['pos_session_closing_confirmation.pos_session_closing_confirmation'].search([]),
#         })

#     @http.route('/pos_session_closing_confirmation/pos_session_closing_confirmation/objects/<model("pos_session_closing_confirmation.pos_session_closing_confirmation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_session_closing_confirmation.object', {
#             'object': obj
#         })
