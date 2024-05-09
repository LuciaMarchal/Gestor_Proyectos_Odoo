from odoo import models, fields, api
from datetime import datetime

class TimeTracking(models.Model):
    _name = 'project_time_tracking.project_time_tracking'
    _description = 'Time Tracking model'
    
    name = fields.Char(required=True)
    task_id = fields.Many2one('project_mng.task', string='Task', required=True)
    employee_id = fields.Many2one('project_mng.employee', default=lambda self: self.env.user.id, readonly=True)
    start_time = fields.Datetime(default=datetime.now(), required=True)
    end_time = fields.Datetime()
    duration = fields.Float(compute='_compute_duration', store=True)
    project_id = fields.Many2one('project_mng.project', required=True)
    
    @api.depends('start_time', 'end_time')
    def _compute_duration(self):
        for record in self:
            if record.start_time and record.end_time:
                delta = record.end_time - record.start_time
                record.duration = delta.total_seconds() / 3600.0
            else:
                record.duration = 0.0
                
    @api.onchange('project_id')
    def _onchange_project_id(self):
        if self.project_id:
            return {'domain': {'task_id': [('project_id', '=', self.project_id.id)]}}
    
    @api.onchange('task_id')
    def _onchange_task_id(self):
        if self.task_id:
            self.project_id = self.task_id.project_id.id
