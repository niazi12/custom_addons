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

    in_time = fields.Float(string="Office In Time", digits=(12, 2), copy=False)
    out_time = fields.Float(string="Office Out Time", digits=(12, 2), copy=False)
    working_hour = fields.Float(compute="_value_pc", store=True)
    report_date = fields.Date(string="Offer Start Date",default=lambda self: fields.Date.today())   
    achievement = fields.Text(string='Achievement')
    problems = fields.Text(string='Problems')
    solutions = fields.Text(string='Solutions')

    @api.depends('in_time','out_time')
    def _value_pc(self):
        for record in self:
            record.working_hour = float(record.out_time - record.in_time)

    