from odoo import models, fields

class Project(models.Model):
    _name = 'project.project'
    _description = 'Project model'
    
    name = fields.Char()
    description = fields.Text()
    initial_date = fields.Date()
    final_date = fields.Date()
    worker_ids = fields.One2many('project.employee', 'project_id', string='Workers')
    color = fields.Integer()
    
    task_ids = fields.One2many('project.task', 'project_id', string='tasks')
    document_ids = fields.One2many('project.document', 'project_id', string='Documents')
    report_ids = fields.One2many('project.report', 'project_id', string='Reports')