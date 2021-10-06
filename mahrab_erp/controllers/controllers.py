# -*- coding: utf-8 -*-
# from odoo import http


# class MahrabErp(http.Controller):
#     @http.route('/mahrab_erp/mahrab_erp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mahrab_erp/mahrab_erp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mahrab_erp.listing', {
#             'root': '/mahrab_erp/mahrab_erp',
#             'objects': http.request.env['mahrab_erp.mahrab_erp'].search([]),
#         })

#     @http.route('/mahrab_erp/mahrab_erp/objects/<model("mahrab_erp.mahrab_erp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mahrab_erp.object', {
#             'object': obj
#         })
