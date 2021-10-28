# -*- coding: utf-8 -*-
from odoo import http

from odoo.http import request
   

 
class EmployeeList(http.Controller):
   
    @http.route('/exams', website=True, auth='user')
    def academy_exam(self, **kw):
        exams = request.env['apprisal.employee'].sudo().search([])
        return request.render("apprisal.emloyee_page", {
            'exams': exams
        })