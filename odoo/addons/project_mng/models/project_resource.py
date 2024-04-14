from odoo import models, fields

class Resource(models.Model):
    _name = 'project.resource'
    _description = 'Resource model'
    
    description = fields.Text()
    type = fields.Selection([
        ('key', 'value')
    ])
    availability = fields.Integer()

