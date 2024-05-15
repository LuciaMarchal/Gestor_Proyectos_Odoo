from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project_mng.project'

    total_duration = fields.Float(compute='_compute_total_duration', store=True)
    
    @api.depends('task_ids.total_duration')
    def _compute_total_duration(self):
        for record in self:
            total_duration = sum(record.task_ids.mapped('total_duration'))
            record.total_duration = total_duration
