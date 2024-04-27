from odoo import models, fields
from datetime import datetime

class Resource(models.Model):
    _name = 'project_mng.document'
    _description = 'Resource model'

    name = fields.Char()
    description = fields.Text()
    file = fields.Binary()
    date = fields.Date(default=datetime.today())
    project_id = fields.Many2one('project_mng.project', string='Project')