# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ractivity_reports(models.Model):
    _name = 'daily_report.activity'
    _description = 'daily_report.activity'

    report = fields.Many2one('daily_report.reports',string='report')   
    start_time = fields.Float(string="Office In Time", digits=(12, 2), copy=False)
    end_time = fields.Float(string="Office Out Time", digits=(12, 2), copy=False)
    activity = fields.Text(string='Activity')
    