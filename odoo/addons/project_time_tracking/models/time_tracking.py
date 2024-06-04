# Copyright 2024 Lucia Marchal <lucia.marchal@educa.madrid.com>

from odoo import models, fields, api

class TimeTracking(models.Model):
    _name = 'project_time_tracking.project_time_tracking'
    _description = 'Time Tracking model'
    
    name = fields.Char(required=True)
    task_id = fields.Many2one('project_mng.task', string='Task', required=True)
    user_id = fields.Many2one('res.users', string='Employee', default=lambda self: self.env.user.id, readonly=True)
    start_time = fields.Datetime(default=fields.Datetime.now, required=True)
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

    @api.model
    def create(self, vals):
        record = super(TimeTracking, self).create(vals)
        if record.task_id:
            record.task_id._compute_total_duration()
        return record
    
    def write(self, vals):
        result = super(TimeTracking, self).write(vals)
        for record in self:
            if record.task_id:
                record.task_id._compute_total_duration()
        return result
    
    def unlink(self):
        tasks = self.mapped('task_id')
        result = super(TimeTracking, self).unlink()
        for task in tasks:
            task._compute_total_duration()
        return result
