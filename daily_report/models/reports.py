# -*- coding: utf-8 -*-

from odoo import models, fields, api


class reports(models.Model):
    _name = 'daily_report.reports'
    _description = 'daily_report.daily_report'

    def _default_employee_name(self):
        return self.env.user.employee_id

    
    def _default_employee_department(self):
        return self.env.user.department_id.id

    employee = fields.Many2one('hr.employee', string="Employee", default=_default_employee_name, required=True, ondelete='cascade', index=True,readonly=False)
    department = fields.Many2one('hr.department',string='Department',default=_default_employee_department, required=True, ondelete='cascade', index=True,readonly=False)
    
    in_time = fields.Float(string="Office In Time", digits=(12, 2), copy=False)
    out_time = fields.Float(string="Office Out Time", digits=(12, 2), copy=False)
    working_hour = fields.Float(compute="_value_pc", store=True)
    report_date = fields.Date(string="Offer Start Date",default=lambda self: fields.Date.today())
    mail_sent = fields.Boolean(default=False,string="Mail Sent")
    activity = fields.One2many('daily_report.activity','report',string="Activities")
    achievement = fields.Text(string='Achievement')
    problems = fields.Text(string='Problems')
    solutions = fields.Text(string='Solutions')

    @api.depends('in_time','out_time')
    def _value_pc(self):
        # import pdb
        # pdb.set_trace()
        for record in self:
            record.working_hour = float(record.out_time - record.in_time)

   