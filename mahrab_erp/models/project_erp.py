from odoo import models, fields, api
import datetime

class ErpProject(models.Model):
    _inherit = 'project.project'
    _description = 'Project'

    name = fields.Char(string='Name')

    projectid = fields.Char(string="Project ID")
    p_department = fields.Char(string="Department")
    p_department_head = fields.Char(string="Department Head")
    project_status = fields.Selection([
                ('complete', 'Complete'),
                ('running', 'Running')],
                string='Project Status')
    project_type = fields.Selection([
                ('sm_easy', 'Small and Easy'),
                ('medium', 'Medium'),
                ('hard', 'Hard'),],
                string='Project Type')

    last_modified_on = fields.Date(string='Last Modified on')
    created_on = fields.Date(string='Created on')
    start_date = fields.Date(string='Start Date')
    project_close_date = fields.Date(string='Project Close Date')