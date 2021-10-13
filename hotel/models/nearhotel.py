# -*- coding: utf-8 -*-

from odoo import models, fields, api


class NearHotel(models.Model):
    _name = 'near.hotel'
    _description = 'Near By Hotel'

    

    name = fields.Char(string="Hotel Name")
    description = fields.Text()
    address = fields.Char(string="Address")
    location = fields.Char(string="Location")

    available_rooms = fields.Integer(string="Available Rooms")
    bookhotel_ids = fields.One2many('book.hotel','hotel',string='Book Hotel',index=True)
    hotel_type = fields.Selection([
      
        ('single', 'Single'),
        ('double', 'Double')
    ], string='Room Type')

    def action_hotel_confirm(self):
        self.hotel_type = 'single'
        
    def book_now(self):
        return{
            'res_model': 'book.hotel',
            'type': 'ir.actions.act_window',
            'view_mode':'form',
            'view_type': 'form',
            'view_id' : self.env.ref('hotel.book_form').id,
            'target': 'new',
            'context': {'default_hotel':self.id,}
        }
    
