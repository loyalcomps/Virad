# -*- coding: utf-8 -*-
# from odoo import http


# class PosCustomerRequired(http.Controller):
#     @http.route('/pos_customer_required/pos_customer_required/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_customer_required/pos_customer_required/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_customer_required.listing', {
#             'root': '/pos_customer_required/pos_customer_required',
#             'objects': http.request.env['pos_customer_required.pos_customer_required'].search([]),
#         })

#     @http.route('/pos_customer_required/pos_customer_required/objects/<model("pos_customer_required.pos_customer_required"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_customer_required.object', {
#             'object': obj
#         })
