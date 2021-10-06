
from odoo import models, fields, api
    

class HotelBook(models.Model):
    _name = 'book.hotel'
    _description = 'Book a Hotel'

    def _default_user(self):
        return self.env.user.id
    
    statusID = fields.Selection([
      
        ('approve', 'Approved'),
        ('reject', 'Rejected')
    ], string='Booking Status', default='reject')

    def approve_booking(self):
        for record in self:
        
            record.statusID = 'approve'
            

    def reject_booking(self):
        for record in self:
            
            record.statusID = 'reject'
            

    user = fields.Many2one('res.users', string="User", default=_default_user, required=True, ondelete='cascade', index=True,readonly=True)

    hotel = fields.Many2one('near.hotel',string="Hotels")
    customer_name = fields.Char(string="Customer Name")
    customer_address = fields.Char(string="Customer Address")
    customer_number = fields.Char(string="Members")
    expected_room = fields.Integer(string="Expected Room")
