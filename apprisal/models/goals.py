from odoo import models, fields, api


class CreateGoals(models.Model):
    _name = 'goals.appraisal'
    _description = 'Appraisal'

    name = fields.Char(string='Name of Goal', required=True)