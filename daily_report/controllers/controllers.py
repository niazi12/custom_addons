# -*- coding: utf-8 -*-
# from odoo import http


# class DailyReport(http.Controller):
#     @http.route('/daily_report/daily_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/daily_report/daily_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('daily_report.listing', {
#             'root': '/daily_report/daily_report',
#             'objects': http.request.env['daily_report.daily_report'].search([]),
#         })

#     @http.route('/daily_report/daily_report/objects/<model("daily_report.daily_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('daily_report.object', {
#             'object': obj
#         })
