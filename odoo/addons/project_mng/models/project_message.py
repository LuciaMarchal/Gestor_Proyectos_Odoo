# Copyright 2024 Lucia Marchal <lucia.marchal@educa.madrid.com>

from odoo import models, fields
from datetime import datetime

class Message(models.Model):
    _name = 'project_mng.message'
    _description = 'Message model'

    text = fields.Text(required=True)
    date_time = fields.Datetime(default=datetime.now(), readonly=True)
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user.id, readonly=True)
    project_id = fields.Many2one('project_mng.project', string='Project')
    is_favorite = fields.Boolean()
