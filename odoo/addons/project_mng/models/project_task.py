from odoo import models, fields

class Task(models.Model):
    _name = 'project.task'
    _description = 'Task model'
    
    name = fields.Char('name')
    description = fields.Text('description')
    initial_date = fields.Date('initial_date')
    final_date = fields.Date('final_date')
    state = fields.Selection([
        ('key', 'value')
    ], string='state')
    manager_id = fields.Many2one('project.employee', string='manager')
    project_id = fields.Many2one('project.project', string='project')
    
    comment_ids = fields.One2many('project.comment', 'task_id', string='Comments')