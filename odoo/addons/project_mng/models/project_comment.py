from odoo import models, fields

class Resource(models.Model):
    _name = 'project.comment'
    _description = 'Resource model'

    text = fields.Text('text')
    date_time = fields.Datetime('date_time')
    user_id = fields.Many2one('project.employee', string='user')
    task_id = fields.Many2one('project.task', string='task')
    
    