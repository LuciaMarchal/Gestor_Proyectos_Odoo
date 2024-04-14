from odoo import models, fields

class Resource(models.Model):
    _name = 'project.comment'
    _description = 'Resource model'

    text = fields.Text()
    date_time = fields.Datetime()
    user_id = fields.Many2one('project.employee', string='User')
    task_id = fields.Many2one('project.task', string='Task')
    
    