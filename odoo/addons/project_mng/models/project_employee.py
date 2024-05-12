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
    ])
    department = fields.Char()
    email = fields.Char(required=True)
    phone = fields.Char()
    user_id = fields.Many2one('res.users', string='User')
    
    project_id = fields.Many2one('project_mng.project', string='Project')
    message_ids = fields.One2many('project_mng.message', 'user_id', string='Messages')
    task_ids = fields.One2many('project_mng.task', 'worker_id', string='Tasks')
    
    @api.onchange('name', 'surnames')
    def _onchange_employee(self):
        for record in self:
            if record.email:
                user = self.env['res.users'].search([('login', '=', self.email)], limit=1)
                if user:
                    user.write({
                        "name": record.name + " " + record.surnames,
                    })
            
    @api.model
    def create(self, values):
        employee = super(Employee, self).create(values)
        user = self.env['res.users'].search([('login', '=', values.get('email'))], limit=1)
        if user:
            values['user_id'] = user.id
        else:
            user_values = {
                'name': values.get('name') + " " + values.get('surnames'),
                'login': values.get('email'),
                'password': 'contrasena', 
                'groups_id': [(6, 0, [self.env.ref('base.group_user').id])],
            }
            self.env['res.users'].create(user_values)
        return employee
    
