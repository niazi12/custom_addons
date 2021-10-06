from odoo import models, fields, api

class shop(models.Model):
    _inherit = 'product.template'

    name =  fields.Char(string='Course Name')
    course_id =  fields.Char(string='Course Code')