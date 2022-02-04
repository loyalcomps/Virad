# -*- coding: utf-8 -*-
# from odoo import http


# class PosLocationAsCustomer(http.Controller):
#     @http.route('/pos_location_as_customer/pos_location_as_customer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_location_as_customer/pos_location_as_customer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_location_as_customer.listing', {
#             'root': '/pos_location_as_customer/pos_location_as_customer',
#             'objects': http.request.env['pos_location_as_customer.pos_location_as_customer'].search([]),
#         })

#     @http.route('/pos_location_as_customer/pos_location_as_customer/objects/<model("pos_location_as_customer.pos_location_as_customer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_location_as_customer.object', {
#             'object': obj
#         })
