from odoo import models, fields

class contacts_information(models.Model):
    _name = 'contact.info'
    _description = 'Here contact information is stored.'

    name = fields.Char(string='Name')
    phone_number = fields.Char(string='Phone No.')
    address = fields.Char(string='Address')
    #photo = fields.Binary(string="Photo", attachment=True)