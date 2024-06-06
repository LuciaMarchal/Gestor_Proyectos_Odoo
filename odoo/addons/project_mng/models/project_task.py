# Copyright 2024 Lucia Marchal <lucia.marchal@educa.madrid.com>

from odoo import models, fields
from datetime import datetime

class Task(models.Model):
    _name = 'project_mng.task'
    _description = 'Task model'
    
    name = fields.Char(required=True)
    description = fields.Text(required=True)
    initial_date = fields.Date()
    state = fields.Selection([
        ('to_do', 'To do'),
        ('doing', 'Doing'),
        ('testing', 'Testing'),
        ('displayed', 'Displayed'),
        ('done', 'Done'),
        ('closed', 'Closed'),
        ('canceled', 'Canceled')
    ], default="to_do", required=True)
    worker_id = fields.Many2one('project_mng.employee', string='Worker')
    project_id = fields.Many2one('project_mng.project', string='Project')
    comment = fields.Text()
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
        ('3', 'Very High')
    ])
    handle_widget = fields.Char()

