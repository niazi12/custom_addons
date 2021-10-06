# -*- coding: utf-8 -*-
from odoo import http

from odoo.http import request
# class NiaziAcademy(http.Controller):
#     @http.route('/niazi__academy/niazi__academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/niazi__academy/niazi__academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('niazi__academy.listing', {
#             'root': '/niazi__academy/niazi__academy',
#             'objects': http.request.env['niazi__academy.niazi__academy'].search([]),
#         })

#     @http.route('/niazi__academy/niazi__academy/objects/<model("niazi__academy.niazi__academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('niazi__academy.object', {
#             'object': obj
#         })
    

class Property(http.Controller):

    @http.route('/request', type="http", auth="public", website=True)
    def request(self, **kw):
        print("Execution Here.........................")  
        course_list = request.env['academy.course'].sudo().search([])   
        return http.request.render('niazi__academy.create_property', {
            'course_list': course_list
        })
    
    @http.route('/request/property', type="http", auth="public", website=True)
    def request_property(self, **kw):
        
        print("Data Received.....", kw)
        request.env['academy.faculty'].sudo().create(kw)
        return request.render("niazi__academy.property_thanks", {})
    
    
    
   
class facultyList(http.Controller):
    # @http.route('/get_exams', type='http', auth='public')
    # def get_exams(self):
    #     print("Yes here entered")
    #     exams_rec = request.env['academy.faculty'].search([])
    #     exams = []
    #     for rec in exams_rec:
    #         vals = {
    #             'name': rec.name,
    #         }
    #         exams.append(vals)
    #     print("Exam List--->", exams)
    #     data = {'status': 200, 'response': exams, 'message': 'Final Exam is Over'}
    #     return data

    @http.route('/exams', website=True, auth='user')
    def academy_exam(self, **kw):
        exams = request.env['academy.faculty'].sudo().search([])
        return request.render("niazi__academy.exam_page", {
            'exams': exams
        })