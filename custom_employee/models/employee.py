from odoo import models, fields, api
from dateutil.relativedelta import relativedelta 
from odoo.exceptions import ValidationError
import re 

class Employee(models.Model):
    _name = 'create.employee'
    _description = 'employee'
    

    projectName_id =  fields.Many2one('create.project', string="Project")
    roleName_id =  fields.Many2one('create.role', string="Role")
    responsibilty = fields.Text(string='Responsibility')
    technology_ids = fields.Many2many('employee.technology', string="Technology")
    process_ids = fields.Many2many('create.process', string="Process")

    from_date = fields.Date(string="From")
    to_date = fields.Date(string="To")
    duation = fields.Integer(string="Duration")

    member = fields.Integer(string="No. of Member")
    # @api.depends('from_date','to_date')
    # def _duration(self):
    #     for record in self:
    #         record.duation = relativedelta(record.to_date - record.from_date)
    employees = fields.Many2one('hr.employee', string='Employee')
    @api.constrains('from_date','to_date')
    def _check_date_validation(self):
        for record in self:
            if record.from_date > record.to_date:
                raise ValidationError('Put a valid date ')

class CreateProject(models.Model):
    _name = 'create.project'
    _description = 'Project'
    _rec_name = 'projectName'
    projectName = fields.Char(string='Project')

class CreateRoles(models.Model):
    _name = 'create.role'
    _description = 'Role'
    _rec_name = 'roleName'

    roleName = fields.Char(string='Role')
    manyOne =  fields.Many2one('create.employee', string="EM")

class CreateTechnology(models.Model):
    _name = 'employee.technology'
    _description ='Technology'
    _rec_name = 'technology_name'

    technology_name = fields.Char(string="Technology Name")
    description = fields.Char(string="Description")
    manyOne =  fields.Many2one('create.employee', string="EM")

class CreateProcess(models.Model):
    _name = 'create.process'
    _description = 'Process'
    _rec_name = 'processName'
    
    processName = fields.Char(string='Process')
    manyOne =  fields.Many2one('create.employee', string="EM")

      


   