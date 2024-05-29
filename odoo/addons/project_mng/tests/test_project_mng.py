from odoo.addons.project_mng.common import TestProjectMngCommon
from datetime import datetime, timedelta
from odoo.tests.common import TransactionCase

class TestProjectMng(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super(TestProjectMng, cls).setUpClass()
        cls.Project = cls.env['project_mng.project']
        cls.Task = cls.env['project_mng.task']
        cls.Employee = cls.env['project_mng.employee']
        cls.User = cls.env['res.users']
        
        cls.project = cls.Project.create({
            'name': 'Test Project',
        })
        cls.employee1 = cls.Employee.create({'name': 'Employee 1'})
        cls.employee2 = cls.Employee.create({'name': 'Employee 2'})

    # REPORTS
    def test_report_creation(self):
        report = self.Report.create({
            'project_id': self.project.id,
        })

        self.assertTrue(report)
        self.assertEqual(report.project_id, self.project)
        self.assertTrue(report.name)
        self.assertEqual(report.date, datetime.today().date())

    def test_sequence_generated_for_report(self):
        report = self.Report.create({
            'project_id': self.project.id
        })

        self.assertTrue(report.name)
        self.assertTrue(report.name.startswith('REP'))  

    # PROJECT
    def test_project_creation(self):
        initial_date = datetime.today().date()
        final_date = initial_date + timedelta(days=30)
        project = self.Project.create({
            'name': 'Test Project',
            'description': 'Project Description',
            'initial_date': initial_date,
            'final_date': final_date,
        })
        
        self.assertTrue(project)
        self.assertEqual(project.name, 'Test Project')
        self.assertEqual(project.description, 'Project Description')
        self.assertEqual(project.initial_date, initial_date)
        self.assertEqual(project.final_date, final_date)
        self.assertEqual(project.state, 'first_impressions')

    def test_action_change_state(self):
        project = self.Project.create({
            'name': 'Test Project',
            'description': 'Project Description',
            'initial_date': datetime.today().date(),
            'final_date': datetime.today().date() + timedelta(days=30),
        })
        
        states = [
            'to_do', 'doing', 'testing', 'displayed', 'done', 'closed'
        ]
        
        for state in states:
            project.action_change_state()
            self.assertEqual(project.state, state)

    def test_action_cancel(self):
        project = self.Project.create({
            'name': 'Test Project',
            'description': 'Project Description',
            'initial_date': datetime.today().date(),
            'final_date': datetime.today().date() + timedelta(days=30),
        })
        
        project.action_cancel()
        self.assertEqual(project.state, 'canceled')

    def test_compute_worker_ids(self):
        project = self.Project.create({
            'name': 'Test Project',
            'description': 'Project Description',
            'initial_date': datetime.today().date(),
            'final_date': datetime.today().date() + timedelta(days=30),
        })

        task1 = self.Task.create({
            'name': 'Task 1',
            'project_id': project.id,
            'worker_id': self.employee1.id
        })

        task2 = self.Task.create({
            'name': 'Task 2',
            'project_id': project.id,
            'worker_id': self.employee2.id
        })
        
        project._compute_worker_ids()
        self.assertIn(self.employee1, project.worker_ids)
        self.assertIn(self.employee2, project.worker_ids)

    # EMPLOYEES
    def test_employee_creation(self):
        employee = self.Employee.create({
            'name': 'John',
            'surnames': 'Doe',
            'job_title': 'developer',
            'department': 'IT',
            'email': 'john.doe@example.com',
            'phone': '123456789',
        })
        
        self.assertTrue(employee)
        self.assertEqual(employee.name, 'John')
        self.assertEqual(employee.surnames, 'Doe')
        self.assertEqual(employee.job_title, 'developer')
        self.assertEqual(employee.department, 'IT')
        self.assertEqual(employee.email, 'john.doe@example.com')
        self.assertEqual(employee.phone, '123456789')

    def test_onchange_employee(self):
        employee = self.Employee.create({
            'name': 'John',
            'surnames': 'Doe',
            'email': 'john.doe@example.com',
        })

        user = self.User.create({
            'name': 'Old Name',
            'login': 'john.doe@example.com',
            'password': 'password'
        })

        employee.name = 'Jane'
        employee.surnames = 'Smith'
        employee._onchange_employee()

        user.refresh()
        self.assertEqual(user.name, 'Jane Smith')

    def test_create_employee_with_user(self):
        employee = self.Employee.create({
            'name': 'John',
            'surnames': 'Doe',
            'email': 'john.doe@example.com',
        })

        user = self.User.search([('login', '=', 'john.doe@example.com')], limit=1)
        
        self.assertTrue(user)
        self.assertEqual(user.name, 'John Doe')
        self.assertEqual(user.login, 'john.doe@example.com')

    def test_create_employee_existing_user(self):
        user = self.User.create({
            'name': 'Existing User',
            'login': 'existing.user@example.com',
            'password': 'password'
        })

        employee = self.Employee.create({
            'name': 'John',
            'surnames': 'Doe',
            'email': 'existing.user@example.com',
        })

        self.assertEqual(employee.user_id, user)
