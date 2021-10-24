from odoo import models, fields, api


class CreateReporting(models.Model):
    _name = 'create.report'
    _description = 'Reporting'

    name =  fields.Many2one('apprisal.employee', string="Employee", required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], related='name.gender')
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