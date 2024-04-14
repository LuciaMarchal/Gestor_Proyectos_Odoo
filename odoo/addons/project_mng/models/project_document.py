from odoo import models, fields

class Resource(models.Model):
    _name = 'project.document'
    _description = 'Resource model'

    name = fields.Char()
    description = fields.Text()
    type = fields.Selection([
        ('key', 'value')
    ])
    file = fields.Binary()
    date = fields.Date()
    project_id = fields.Many2one('project.project', string='Project')