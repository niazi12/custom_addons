from dateutil.relativedelta import relativedelta
from odoo import api, models, _

class PropertyCardReport(models.AbstractModel):
    _name = 'report.real_estate.property_report'
    _description = 'Property card Report'

    @api.model
    def _get_report_values(self, docids, data=None):

        

        docs = self.env['real.estate'].browse(docids[0])
        buyers = self.env['res.users'].search([('property_ids', '=', docids[0])])

        print(buyers)

        buyer_lists = []

        for buyer in buyers:
            vals = {
                'name': buyer.name
            }

            buyer_lists.append(vals)

        return {
            'doc_model': 'real.estate',
            'data': data,
            'docs': docs,
            'buyer_lists': buyer_lists,
        }