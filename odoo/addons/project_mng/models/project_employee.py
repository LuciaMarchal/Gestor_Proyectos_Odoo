from odoo import models, fields

class Employee(models.Model):
    _name = 'project.employee'
    _description = 'Employee model'

    name = fields.Char()
    surnames = fields.Char()
    job_title = fields.Selection([
        ('key', 'value')
    ])
    department = fields.Char()
    email = fields.Char()
    phone = fields.Char()
    #usuario de odoo
    
    project_id = fields.Many2one('project.project', string='Project')
    comment_ids = fields.One2many('project.comment', 'user_id', string='Comments')
    task_ids = fields.One2many('project.task', 'worker_id', string='Tasks')