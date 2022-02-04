# -*- coding: utf-8 -*-
# from odoo import http


# class PosUserRestrict(http.Controller):
#     @http.route('/pos_user_restrict/pos_user_restrict/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_user_restrict/pos_user_restrict/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_user_restrict.listing', {
#             'root': '/pos_user_restrict/pos_user_restrict',
#             'objects': http.request.env['pos_user_restrict.pos_user_restrict'].search([]),
#         })

#     @http.route('/pos_user_restrict/pos_user_restrict/objects/<model("pos_user_restrict.pos_user_restrict"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_user_restrict.object', {
#             'object': obj
#         })
