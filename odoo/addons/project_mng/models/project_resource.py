from odoo import models, fields

class Resource(models.Model):
    _name = 'project.resource'
    _description = 'Resource model'
    
    description = fields.Text('description')
    type = fields.Selection([
        ('key', 'value')
    ], string='type')
    availability = fields.Integer('availability')

