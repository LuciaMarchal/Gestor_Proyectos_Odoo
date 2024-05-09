from odoo import models, fields

class Resource(models.Model):
    _name = 'project_mng.resource'
    _description = 'Resource model'
    
    name = fields.Char(compute='_compute_name', store=True, readonly=True)
    description = fields.Text()
    type = fields.Selection([
        ('human_resources', 'Human Resources'),
        ('materials', 'Materials'),
        ('financial', 'Financial'),
        ('other', 'Other'),
    ], required=True)
    availability = fields.Integer(required=True)
    
    def _compute_name(self):
        for resource in self:
            if resource.type:
                resource.name = dict(self._fields['type'].selection).get(resource.type)
