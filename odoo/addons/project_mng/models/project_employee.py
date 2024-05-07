from odoo import models, fields, _

class Employee(models.Model):
    _name = 'project_mng.employee'
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
    user_id = fields.Many2one('res.users', string='User', ondelete="cascade")
    
    project_id = fields.Many2one('project_mng.project', string='Project')
    message_ids = fields.One2many('project_mng.message', 'user_id', string='Messages')
    task_ids = fields.One2many('project_mng.task', 'worker_id', string='Tasks')
    
    def action_update_user(self):
        user = self.env['res.users'].search([('login', '=', self.email)])
        
        if user:
            user.write(
                {"name": self.name},
                {"login": self.email},
            )
        else:
            user_vals = {
                'name': self.name,
                'login': self.email,
                'password': 'contrasena', 
                'groups_id': [(6, 0, [
                    self.env.ref('base.group_user').id
                ])],
                'notification_type': 'inbox'
            }
            self.env['res.users'].create(user_vals)
        # return {
        #     "type": "ir.action.client",
        #     "name": _("Employees"),
        #     "conext": self.env.context,
        #     "model": "res.users",
        # }
