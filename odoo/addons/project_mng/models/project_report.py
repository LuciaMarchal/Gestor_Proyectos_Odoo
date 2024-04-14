from odoo import models, fields

class Report(models.Model):
    _name = 'project.report'
    _description = 'Report model'

    name = fields.Char()
    description = fields.Text()
    type = fields.Selection([
        ('key', 'value')
    ])
    file = fields.Binary()
    date = fields.Date()
    project_id = fields.Many2one('project.project', string='Project')