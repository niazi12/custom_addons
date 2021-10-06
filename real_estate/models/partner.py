from odoo import models, fields, api




class ResUser(models.Model):
    _inherit = 'res.users'

    owner = fields.Char(string="Owner Name", default=False)
    title_name = fields.Many2many('real.estate', string = "Property Name", readonly=True)