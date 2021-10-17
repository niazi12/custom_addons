from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re    

class CreateEmployee(models.Model):
    _name = 'apprisal.employee'
    _description = 'Create employee'

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female', 'Female')
    ], string='Gender')
    email = fields.Char(string='Email')
    phone = fields.Integer(string='Mobile')
    address = fields.Char(string='Address')
    about = fields.Text(string='About')
    age = fields.Integer(string='Age')
    image = fields.Binary(string='Image', attachment=True)
    employeeID = fields.Integer(string='Employee ID', required=True)
    work_phone = fields.Integer(string='Work Phone')
    joined_from = fields.Date(string='Joined Date')
    designation = fields.Selection([     
        ('hr', 'Hr'),
        ('admin', 'Admin'),
        ('software', 'Software Engineer'),
        ('finance', 'Finance'),
        ('ed', 'ED Head'),
        ('ceo', 'Ceo'),
        ('security', 'Security Guard'),
        ('others', 'Others'),
    ], string='Deapartment', required = True)
    work_hour_day = fields.Integer(string='Working hours(day)')

    total_week = fields.Float(String = 'Working hours(week)', compute="_compute_total")
    total_month_hours = fields.Float(String = 'Working hours(months)', compute="_compute_total")
 
    @api.depends("work_hour_day")
    def _compute_total(self):
        for record in self:
            record.total_week = record.work_hour_day * 5
            record.total_month_hours = record.work_hour_day * 20
    
    @api.constrains('email')
    def _check_email(self):
        for record in self:
            valid_email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                                   record.email)

            if valid_email is None:
                raise ValidationError('Please provide a valid E-mail')

    @api.constrains('age')
    def _check_employee_age(self):
        for record in self:
            if record.age <= 0:
                raise ValidationError('Age must be greater than 0')
    
    @api.constrains('phone')
    def _check_employee_phone(self):
        for record in self:
            if record.phone < 0:
                raise ValidationError('Phone must be greater than 0')

    
    
    
    