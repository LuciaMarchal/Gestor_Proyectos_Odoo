from odoo import models, fields

class Comment(models.Model):
    _name = 'project.comment'
    _description = 'Comment model'

    text = fields.Text()
    date_time = fields.Datetime(default=fields.datetime.now(), readonly=True)
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user.id, readonly=True)
    task_id = fields.Many2one('project.task', string='Task')
    project_id = fields.Many2one('project.project', string='Project')
    
