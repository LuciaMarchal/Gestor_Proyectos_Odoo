from odoo import models, fields
from time import time

class Project(models.Model):
    _inherit = 'project_mng.project'

    total_duration = fields.Float(compute='_compute_total_duration')
    
    def _compute_total_duration(self):
        for record in self:
            total_duration = sum(record.task_ids.mapped('total_duration'))
            record.total_duration = total_duration
