from odoo import models, fields, api
from datetime import datetime

class Report(models.Model):
    _name = 'project_mng.report'
    _description = 'Report model'

    name = fields.Char(readonly=True)
    file = fields.Binary()
    date = fields.Date(default=datetime.today(), readonly=True)
    project_id = fields.Many2one('project_mng.project', string='Project')
    
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('report.code')
        result = super(Report, self).create(vals)
        return result

