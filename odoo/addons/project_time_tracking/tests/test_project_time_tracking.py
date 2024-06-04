# Copyright 2024 Lucia Marchal <lucia.marchal@educa.madrid.com>

from odoo.tests.common import TransactionCase
from datetime import datetime, timedelta

class TestTimeTracking(TransactionCase):

    def setUp(self):
        super(TestTimeTracking, self).setUp()
        self.user = self.env['res.users'].create({
            'name': 'Test User',
            'login': 'testuser',
            'email': 'testuser@example.com',
        })
        self.project = self.env['project_mng.project'].create({
            'name': 'Test Project',
        })
        self.task = self.env['project_mng.task'].create({
            'name': 'Test Task',
            'project_id': self.project.id,
        })
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(hours=2)

    def test_create_time_tracking(self):
        record = self.env['project_time_tracking.project_time_tracking'].create({
            'name': 'Test Time Tracking',
            'task_id': self.task.id,
            'user_id': self.user.id,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'project_id': self.project.id,
        })
        self.assertEqual(record.duration, 2.0, "Duration should be 2 hours")

    def test_unlink_time_tracking(self):
        record = self.env['project_time_tracking.project_time_tracking'].create({
            'name': 'Test Time Tracking',
            'task_id': self.task.id,
            'user_id': self.user.id,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'project_id': self.project.id,
        })
        record.unlink()
        self.assertFalse(self.env['project_time_tracking.project_time_tracking'].search([('id', '=', record.id)]), "Record should be deleted")
