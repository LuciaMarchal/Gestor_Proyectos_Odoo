from odoo import models, fields

class Employee(models.Model):
    _name = 'project.employee'
    _description = 'Employee model'

    name = fields.Char('name')
    surnames = fields.Char('surnames')
    job_title = fields.Selection([
        ('key', 'value')
    ], string='job_title')
    department = fields.Char('department')
    email = fields.Char('email')
    phone = fields.Char('phone')
    #usuario de odoo
    
    project_id = fields.Many2one('project.project', string='Project')
    comment_ids = fields.One2many('project.comment', 'user_id', string='Comments')
    task_ids = fields.One2many('project.task', 'manager_id', string='Tasks')