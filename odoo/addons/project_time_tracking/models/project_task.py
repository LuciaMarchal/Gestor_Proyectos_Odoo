# Copyright 2024 Lucia Marchal <lucia.marchal@educa.madrid.com>

from odoo import models, fields, api

class Task(models.Model):
    _inherit = 'project_mng.task'
    
    time_tracking_ids = fields.One2many('project_time_tracking.project_time_tracking', 'task_id')
    total_duration = fields.Float(compute='_compute_total_duration', store=True)
    
    @api.depends('time_tracking_ids.duration')
    def _compute_total_duration(self):
        for record in self:
            record.total_duration = sum(record.time_tracking_ids.mapped('duration'))
