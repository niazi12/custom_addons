from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re 

class HospitalAppointment(models.Model):
    _name = 'create.meetings'
    _description = 'Meetings'
    

    name = fields.Many2one("apprisal.employee", string='Host', required=True)
    meeting_type = fields.Selection([
        ('gbm', 'General Body Meeting'),
        ('interview', 'Interview'),
        ('ceo', 'CEO'),
    ], default='gbm', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Canceled')
    ], default='draft', required=True)
    meeting_date = fields.Datetime(string='Meeting start', default=fields.datetime.now())
    meeting_finish = fields.Datetime(string='Meeting end', required=True)

    @api.constrains('meeting_date', 'meeting_finish')
    def _check_date_validation(self):
        for record in self:
            if record.meeting_finish  < record.meeting_date:
                raise ValidationError('Put a valid date and time.')
    
    member_ids = fields.Many2many('apprisal.employee', string="Member invited")