# Copyright 2024 Lucia Marchal <lucia.marchal@educa.madrid.com>

from odoo import models, fields

class Resource(models.Model):
    _name = 'project_mng.resource'
    _description = 'Resource model'
    
    description = fields.Text()
    type = fields.Selection([
        ('human_resources', 'Human Resources'),
        ('materials', 'Materials'),
        ('financial', 'Financial'),
        ('other', 'Other'),
    ], required=True)
    availability = fields.Integer(required=True)
    