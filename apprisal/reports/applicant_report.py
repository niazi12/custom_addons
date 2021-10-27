from odoo import api, models


class ApplicantReport(models.AbstractModel):
    _name = 'apprisal.report_appraisal'
    _description = 'Applicanrt Profile Report'


    @api.model
    def _get_report_values(self, docids, data=None):
        print("print from applicant report method")
        
        print("self",self)
        print("data",data)
        docs = self.env['create.appraisal'].browse(docids[0])
       
        return {
            'doc_model': 'create.appraisal',
            'data': data,
            'docs': docs,
            
        }
