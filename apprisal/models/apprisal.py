from odoo import models, fields, api
AVAILABLE_PRIORITIES = [
    ('0', 'Normal'),
    ('1', 'Good'),
    ('2', 'Very Good'),
    ('3', 'Excellent')
]

class CreateApprisal(models.Model):
    _name = 'create.appraisal'
    _description = 'Appraisal'

    name =  fields.Many2one('apprisal.employee', string="Employee", required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], related='name.gender')
    apprisal_deadline = fields.Datetime(string='Apprisal Deadline ', default=fields.datetime.now())
    employeeID = fields.Integer(string='Employee ID', required=True, related='name.employeeID')
    designation = fields.Selection([     
        ('hr', 'Hr'),
        ('admin', 'Admin'),
        ('software', 'Software Engineer'),
        ('finance', 'Finance'),
        ('ed', 'ED Head'),
        ('ceo', 'Ceo'),
        ('security', 'Security Guard'),
        ('others', 'Others'),
    ], string='Deapartment', related='name.designation')
    manager =  fields.Many2one('apprisal.employee', string="Manager", required=True)
    manager_feedback = fields.Text(string='Manager Feedback')
    employee_feedback = fields.Text(string='Employee Feedback')
    status = fields.Selection([
      
        ('draft', 'Drafted'),
        ('confirm', 'Confirmed')
    ], string='Status', default='draft')
    priority = fields.Selection(AVAILABLE_PRIORITIES, "Rank", default='0')
    responsibiliy = fields.Text(string='Key Responsibilities')
    employee_responsibiliy = fields.Text(string='Employee Responsibilities')
    accomplishmnet = fields.Text(string='Major Accomplishment & Result')
    manager_rating = fields.Selection([
        ('a', 'Exceeded Expectations'),
        ('b', 'Meet Expectations'),
        ('c', 'Expected Results Not Achieved')
    ], )
    user_id =  fields.Many2one('res.users', string="User ID")
    def approve_appraisal(self):
        for record in self:        
            record.status = 'approve'
            
    def reject_appraisal(self):
        for record in self:           
            record.status = 'reject'

    stage_update = fields.Many2one('appraisal.status', string="Appraisal Status", group_expand='_read_group_stage_ids')

    def book_meeting(self):
        return{
            'res_model': 'create.meetings',
            'type': 'ir.actions.act_window',
            'view_mode':'form',
            'view_type': 'form',
            'view_id' : self.env.ref('apprisal.create_meeting_view_form').id,
            'target': 'new',
            'context': {'default_apprisal':self.id,}
        }

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        stage_ids = self.env['appraisal.status'].search([])
        return stage_ids


class ProductStatus(models.Model):
    _name = "appraisal.status"
    _description = "Appraisal Status"
    _order = 'sequence'

    name = fields.Char("Stage Name", required=True, translate=True)
    sequence = fields.Integer(
        "Sequence", default=10,
        help="Gives the sequence order when displaying a list of stages.")