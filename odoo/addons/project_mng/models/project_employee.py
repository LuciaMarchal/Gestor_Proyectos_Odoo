from odoo import models, fields, api

class Employee(models.Model):
    _name = 'project.employee'
    _description = 'Employee model'

    name = fields.Char()
    surnames = fields.Char()
    job_title = fields.Selection([
        ('manager', 'Project Manager'),
        ('leader', 'Team Leader'),
        ('developer', 'Developer'),
        ('designer', 'Designer'),
        ('tester', 'Tester'),
        ('admin', 'Administrator'),
        ('db_admin', 'Database Administrator'),
        ('intern', 'Intern'),
    ])
    department = fields.Char()
    email = fields.Char()
    phone = fields.Char()
    user_id = fields.Many2one('res.users', string='User')
    
    project_id = fields.Many2one('project.project', string='Project')
    comment_ids = fields.One2many('project.comment', 'user_id', string='Comments')
    task_ids = fields.One2many('project.task', 'worker_id', string='Tasks')
    
    @api.model_create_single
    def create(self, vals):
        employee = super(Employee, self).create(vals)

        user_vals = {
            'name': employee.name,
            'login': employee.email,
            'password': 'contrasena', 
            'groups_id': [(6, 0, [
                self.env.ref('base.group_user').id
            ])]
        }
        self.env['res.users'].create(user_vals)

        return employee