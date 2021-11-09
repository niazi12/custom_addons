from odoo import models, fields, api
class EmployeeQualification(models.Model):
    _inherit = "hr.employee"

    em_ids = fields.One2many('create.employee','employees',string="Project History")