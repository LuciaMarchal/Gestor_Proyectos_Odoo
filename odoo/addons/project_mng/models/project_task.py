from odoo import models, fields

class Task(models.Model):
    _name = 'project.task'
    _description = 'Task model'
    
    name = fields.Char()
    description = fields.Text()
    initial_date = fields.Date()
    final_date = fields.Date()
    state = fields.Selection([
        ('key', 'value')
    ])
    worker_id = fields.Many2one('project.employee', string='Worker')
    project_id = fields.Many2one('project.project', string='Project')
    
    comment_ids = fields.One2many('project.comment', 'task_id', string='Comments')