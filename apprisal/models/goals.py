from odoo import models, fields, api


class CreateGoals(models.Model):
    _name = 'goals.appraisal'
    _description = 'Appraisal'

    name = fields.Char(string='Name of Goal', required=True)
    progression = fields.Selection(selection=[
        ('0', '0 %'),
        ('25', '25 %'),
        ('50', '50 %'),
        ('75', '75 %'),
        ('100', '100 %')
    ], string="Progression", default="0", required=True)
    description = fields.Text(string='Description')
    challanged_by =  fields.Many2one('apprisal.employee', string="Challanged by", required=True)
    deadline = fields.Date(string='Deadline')