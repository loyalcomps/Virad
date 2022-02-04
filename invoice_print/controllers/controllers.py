# -*- coding: utf-8 -*-
# from odoo import http


# class InvoicePrint(http.Controller):
#     @http.route('/invoice_print/invoice_print/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_print/invoice_print/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_print.listing', {
#             'root': '/invoice_print/invoice_print',
#             'objects': http.request.env['invoice_print.invoice_print'].search([]),
#         })

#     @http.route('/invoice_print/invoice_print/objects/<model("invoice_print.invoice_print"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_print.object', {
#             'object': obj
#         })
