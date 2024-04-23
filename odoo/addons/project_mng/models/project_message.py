from odoo import models, fields
from datetime import datetime

class Message(models.Model):
    _name = 'project.message'
    _description = 'Message model'

    text = fields.Text()
    date_time = fields.Datetime(default=fields.datetime.now(), readonly=True)
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user.id, readonly=True)
    project_id = fields.Many2one('project.project', string='Project')
    
