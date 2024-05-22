from odoo.tests import common

class TestProjectMngCommon(common.TransactionCase):
    @classmethod
    def setUpClass(self):
        self.Project = self.env['project_mng.project']
        self.Task = self.env['project_mng.task']
        self.Employee = self.env['project_mng.employee']
        self.User = self.env['res.users']
        
        self.project = self.Project.create({
            'name': 'Test Project',
        })
        self.employee1 = self.Employee.create({'name': 'Employee 1'})
        self.employee2 = self.Employee.create({'name': 'Employee 2'})


