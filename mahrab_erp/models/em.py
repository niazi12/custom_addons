from odoo import models, fields, api

class shop(models.Model):
    _inherit = 'hr.employee'

    skype_id =  fields.Char(string='Skype Id')
    