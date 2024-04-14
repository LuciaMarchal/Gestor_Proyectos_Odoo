from odoo import models, fields

class Resource(models.Model):
    _name = 'project.document'
    _description = 'Resource model'

    name = fields.Char('name')
    description = fields.Text('description')
    type = fields.Selection([
        ('key', 'value')
    ], string='type')
    file = fields.Binary('file')
    date = fields.Date('date')
    project_id = fields.Many2one('project.project', string='project')