from odoo import models, fields
from time import time

class Project(models.Model):
    _name = 'project_mng.project'
    _description = 'Project model'
    
    name = fields.Char(required=True)
    description = fields.Text(required=True)
    initial_date = fields.Date(required=True)
    final_date = fields.Date(required=True)
    worker_ids = fields.Many2many('project_mng.employee', 'project_id', string='Workers')
    color = fields.Integer()
    state = fields.Selection([
        ('first_impressions', 'First impressions'),
        ('to_do', 'To do'),
        ('doing', 'Doing'),
        ('testing', 'Testing'),
        ('displayed', 'Displayed'),
        ('done', 'Done'),
        ('closed', 'Closed'),
        ('canceled', 'Canceled')
    ], default="first_impressions")
    
    task_ids = fields.One2many('project_mng.task', 'project_id', string='tasks')
    document_ids = fields.One2many('project_mng.document', 'project_id', string='Documents')
    report_ids = fields.One2many('project_mng.report', 'project_id', string='Reports')
    message_ids = fields.One2many('project_mng.message', 'project_id', string='Messages')
    resource_ids = fields.Many2many('project_mng.resource', string='Resources')
    
    def action_change_state(self):
        for project in self:
            if project.state == 'first_impressions':
                project.state = 'to_do'
            elif project.state ==  'to_do':
                project.state = 'doing'
            elif project.state ==  'doing':
                project.state = 'testing'
            elif project.state ==  'testing':
                project.state = 'displayed'
            elif project.state ==  'displayed':
                project.state = 'done'
            elif project.state == 'done':
                project.state = 'closed'

    def action_cancel(self):
        for project in self:
            project.state = "canceled"