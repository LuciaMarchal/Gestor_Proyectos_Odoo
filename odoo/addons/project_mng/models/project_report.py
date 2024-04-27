from odoo import models, fields
from datetime import datetime

class Report(models.Model):
    _name = 'project_mng.report'
    _description = 'Report model'

    name = fields.Char()
    description = fields.Text()
    file = fields.Binary()
    date = fields.Date(default=datetime.today(), readonly=True)
    project_id = fields.Many2one('project_mng.project', string='Project')