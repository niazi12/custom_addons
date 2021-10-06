from odoo import models, fields, api

from dateutil.relativedelta import relativedelta
class CreateWizard(models.TransientModel):

    _name= 'realestate.wizard'
    _description= 'Print  Wizard'
    
    name = fields.Char(string = "Name")
    description = fields.Char(string = "Description")
    expected = fields.Date(string = "Available from")

    def print_report(self):
        #customers = self.env['res.users'].search([('property_ids', '=', docids[0])])
        data = {
            'model': 'realestate.wizard',
            'form': self.read()[0]
        }

        return self.env.ref('real_estate.report_real_estate').report_action(self,data=data)


  # def print_report(self):
    #     data = {
    #         'model' : 'kmhospital.appointment',
    #         'form'  : self.read()[0]

    #     }
    #     return self.env.ref('km_hospital.kmhospital_appointment').report_action(self,data=data)
