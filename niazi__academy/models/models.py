
from odoo import models, fields, api

from odoo.exceptions import ValidationError
import re
class AcademyStudent(models.Model):
    _name = 'academy.student'
    _description = 'Academy Students'

    name = fields.Char(string='Name')
    gender = fields.Selection([
        ('male','Male'),
        ('female', 'Female')
    ])
    address = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    course = fields.Char(string='Course')
    note = fields.Text(string='Note')
    responsible_id = fields.Many2one('academy.faculty', string='Supervisor')
    student_id = fields.Many2many('academy.course', string="Course ID")

    @api.constrains('address')
    def _check_email(self):
        for record in self:
            valid_email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', record.address)
            
            if valid_email == None:
                raise ValidationError('Please provide a valid E-mail')

   

class AcademyCourse(models.Model):
    _name = 'academy.course'
    _description = 'Academy Course'

    name = fields.Char(string='Name')
    course_code = fields.Char(string='Course Code')
    credit = fields.Integer(string='Credit')
    note = fields.Text(string='Note')

class AcademyAdmin(models.Model):
    _name = 'academy.admin'
    _description = 'Academy Admin'
  
    name = fields.Char(string='Name')
    id = fields.Char(string='Id Number')

class AcademyFaculty(models.Model):
    _name = 'academy.faculty'
    _description = 'Academy faculty'

    name = fields.Char(string='Name')
    phone = fields.Char(string='Phone')
    course_name = fields.Char(string='Course Name')
    note = fields.Text(string='Note')
    students_list_ids = fields.One2many('academy.student', 'responsible_id', string="Students List")
    include_last_name = fields.Boolean('Include Last name')

   
    course_list = fields.Many2one('academy.course', string= "Courses")
    last_name = fields.Char(string = "Last Name")
    
    

