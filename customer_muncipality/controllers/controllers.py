# -*- coding: utf-8 -*-
# from odoo import http


# class CustomerMuncipality(http.Controller):
#     @http.route('/customer_muncipality/customer_muncipality/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_muncipality/customer_muncipality/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_muncipality.listing', {
#             'root': '/customer_muncipality/customer_muncipality',
#             'objects': http.request.env['customer_muncipality.customer_muncipality'].search([]),
#         })

#     @http.route('/customer_muncipality/customer_muncipality/objects/<model("customer_muncipality.customer_muncipality"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_muncipality.object', {
#             'object': obj
#         })
