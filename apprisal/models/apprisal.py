from odoo import models, fields, api


class CreateApprisal(models.Model):
    _name = 'create.appraisal'
    _description = 'Appraisal'

    name =  fields.Many2one('apprisal.employee', string="Employee", required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], related='name.gender')
    apprisal_deadline = fields.Datetime(string='Apprisal Deadline ', default=fields.datetime.now())
    employeeID = fields.Integer(string='Employee ID', required=True, related='name.employeeID')
    designation = fields.Selection([     
        ('hr', 'Hr'),
        ('admin', 'Admin'),
        ('software', 'Software Engineer'),
        ('finance', 'Finance'),
        ('ed', 'ED Head'),
        ('ceo', 'Ceo'),
        ('security', 'Security Guard'),
        ('others', 'Others'),
    ], string='Deapartment', related='name.designation')