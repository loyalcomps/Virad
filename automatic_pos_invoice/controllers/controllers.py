# -*- coding: utf-8 -*-
# from odoo import http


# class AutomaticPosInvoice(http.Controller):
#     @http.route('/automatic_pos_invoice/automatic_pos_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/automatic_pos_invoice/automatic_pos_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('automatic_pos_invoice.listing', {
#             'root': '/automatic_pos_invoice/automatic_pos_invoice',
#             'objects': http.request.env['automatic_pos_invoice.automatic_pos_invoice'].search([]),
#         })

#     @http.route('/automatic_pos_invoice/automatic_pos_invoice/objects/<model("automatic_pos_invoice.automatic_pos_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('automatic_pos_invoice.object', {
#             'object': obj
#         })
