# -*- coding: utf-8 -*-

from odoo import models, fields, api



class RealEstate(models.Model):
    _name = 'real.estate'
    _description = 'Real Estate'
    _inherits = {'res.users': 'related_user_id'}
    _sql_constraints = [
        ('check_exprected_price', 'CHECK(expected_price >= 0)', 'The expected price must be strictly positive'),
        ('check_selling_price', 'CHECK(selling_price >= 0)', 'The selling price must be positive')
        
    ]
    related_user_id =  fields.Many2one('res.users', string="Customer ID")
    users = fields.Many2many('res.users',string="users")

   #partner_id = fields.Many2one('res.partner',string="Partner ID")

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    expected_price = fields.Float(string='Expected Price')
    bedrooms = fields.Integer(string='Bedrooms')
    facades = fields.Integer(string='Facades')
    garden = fields.Boolean(string='Garden')
    garden_orientation = fields.Selection([
        ('north','North'),
        ('south', 'South')
    ])
    active = fields.Boolean(string='Active')
    available_from = fields.Date(string='Available From')
    date_to = fields.Date(string='Availability Finish')
    selling_price = fields.Integer(string='Selling Price')
    living_area = fields.Integer(string='Living Area (sqm)')
    garage = fields.Boolean(string='Garage')
    status = fields.Selection([
        ('confirm','Confirmed'),
        ('draft', 'Draft')
    ],  default='new')
    area = fields.Integer(string='Garden Area(sqm)')
    def action_status_confirm(self):
        self.status = 'confirm'
    
    def action_status_draft(self):
        self.status = 'draft'

    def action_view_url(self):
        
        return{
            "type": "ir.actions.act_url",
            "url": "https://odoo.com",
            "target": "self",   
        }

    total = fields.Float(compute="_compute_total", inverse="_inverse_total")
 

    @api.depends("living_area", "area",)
    def _compute_total(self):
        for record in self:
            record.total = record.living_area + record.area
    def _inverse_total(self):
        for record in self:
            record.living_area = record.total - record.area
            # record.area = record.total - record.living_area

class employeeRealestate(models.Model):
    _inherit = "hr.department"
    
class ResUsers(models.Model):
    _inherit = "res.users"
    property_ids = fields.One2many(
        "real.estate", "related_user_id", string="Properties"
        )


    
    
