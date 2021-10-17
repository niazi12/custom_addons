# -*- coding: utf-8 -*-
# from odoo import http


# class Apprisal(http.Controller):
#     @http.route('/apprisal/apprisal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/apprisal/apprisal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('apprisal.listing', {
#             'root': '/apprisal/apprisal',
#             'objects': http.request.env['apprisal.apprisal'].search([]),
#         })

#     @http.route('/apprisal/apprisal/objects/<model("apprisal.apprisal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('apprisal.object', {
#             'object': obj
#         })
