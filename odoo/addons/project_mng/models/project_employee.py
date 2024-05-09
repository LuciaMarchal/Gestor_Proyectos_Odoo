from odoo import models, fields, _, api

class Employee(models.Model):
    _name = 'project_mng.employee'
    _description = 'Employee model'

    name = fields.Char(required=True)
    surnames = fields.Char(required=True)
    job_title = fields.Selection([
        ('manager', 'Project Manager'),
        ('leader', 'Team Leader'),
        ('developer', 'Developer'),
        ('designer', 'Designer'),
        ('tester', 'Tester'),
        ('admin', 'Administrator'),
        ('db_admin', 'Database Administrator'),
        ('intern', 'Intern'),
    ], required=True)
    department = fields.Char()
    email = fields.Char(required=True)
    phone = fields.Char()
    user_id = fields.Many2one('res.users', string='User')
    
    project_id = fields.Many2one('project_mng.project', string='Project')
    message_ids = fields.One2many('project_mng.message', 'user_id', string='Messages')
    task_ids = fields.One2many('project_mng.task', 'worker_id', string='Tasks')
    
    @api.onchange('email', 'name', 'surnames')
    def _onchange_user(self):
        if self.email:
            user = self.env['res.users'].search([('login', '=', self.email)])
            if user:
                user.write({
                    "name": self.name + " " + self.surnames,
                    "login": self.email,
                })
            
    @api.model
    def create(self, values):
        employee = super(Employee, self).create(values)
        user = self.env['res.users'].search([('login', '=', values.get('email'))], limit=1)
        if user:
            values['user_id'] = user.id
        else:
            user_values = {
                'name': values.get('name'),
                'login': values.get('email'),
                'password': 'contrasena', 
                'groups_id': [(6, 0, [self.env.ref('base.group_user').id])],
            }
            self.env['res.users'].create(user_values)
        return employee
    
