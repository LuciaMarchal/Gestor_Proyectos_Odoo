from odoo import models, fields, api
from datetime import datetime

class Task(models.Model):
    _name = 'project_mng.task'
    _description = 'Task model'
    
    name = fields.Char()
    description = fields.Text()
    initial_date = fields.Date(default=datetime.today(), readonly=True)
    final_date = fields.Date()
    state = fields.Selection([
        ('to_do', 'To do'),
        ('doing', 'Doing'),
        ('testing', 'Testing'),
        ('displayed', 'Displayed'),
        ('done', 'Done'),
        ('closed', 'Closed'),
        ('canceled', 'Canceled')
    ], default="to_do")
    worker_id = fields.Many2one('project_mng.employee', string='Worker')
    project_id = fields.Many2one('project_mng.project', string='Project')
    comment = fields.Text()
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
        ('3', 'Very High')
    ])
    
