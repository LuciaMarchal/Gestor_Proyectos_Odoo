from odoo import models, fields

class Report(models.Model):
    _name = 'project.report'
    _description = 'Report model'

    name = fields.Char('name')
    description = fields.Text('description')
    type = fields.Selection([
        ('key', 'value')
    ], string='type')
    file = fields.Binary('file')
    date = fields.Date('date')
    project_id = fields.Many2one('project.project', string='project')