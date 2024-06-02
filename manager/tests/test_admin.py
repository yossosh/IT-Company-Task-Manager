from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from manager.admin import PositionAdmin, TaskTypeAdmin, TagAdmin, WorkerAdmin, TaskAdmin
from manager.models import Position, TaskType, Tag, Worker, Task


class AdminTests(TestCase):

    def setUp(self):
        self.site = AdminSite()
        self.position = Position.objects.create(name="Developer")
        self.task_type = TaskType.objects.create(name="Bugfix")
        self.tag = Tag.objects.create(name="Urgent")
        self.worker = Worker.objects.create_user(
            username="worker", password="password", position=self.position
        )
        self.task = Task.objects.create(
            name="Fix Bug",
            description="Fix critical bug",
            deadline="2023-12-31",
            priority="High",
            task_type=self.task_type,
        )
        self.task.assignees.add(self.worker)

    def test_position_admin(self):
        ma = PositionAdmin(Position, self.site)
        self.assertEqual(list(ma.list_display), ["name"])

    def test_task_type_admin(self):
        ma = TaskTypeAdmin(TaskType, self.site)
        self.assertEqual(list(ma.list_display), ["name"])

    def test_tag_admin(self):
        ma = TagAdmin(Tag, self.site)
        self.assertEqual(list(ma.list_display), ["name"])

    def test_worker_admin(self):
        ma = WorkerAdmin(Worker, self.site)
        self.assertEqual(list(ma.list_display), ["username", "position"])

    def test_task_admin(self):
        ma = TaskAdmin(Task, self.site)
        self.assertEqual(list(ma.list_display), ["name", "priority", "task_type"])
