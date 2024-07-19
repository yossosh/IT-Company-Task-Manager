from django.core.exceptions import ValidationError
from django.test import TestCase
from manager.models import Position, TaskType, Tag, Worker, Task
from django.utils import timezone


class PositionModelTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")

    def test_position_str(self):
        self.assertEqual(str(self.position), "Developer")


class TaskTypeModelTest(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="Bugfix")

    def test_task_type_str(self):
        self.assertEqual(str(self.task_type), "Bugfix")


class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Urgent")

    def test_tag_str(self):
        self.assertEqual(str(self.tag), "Urgent")


class WorkerModelTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.worker = Worker.objects.create_user(
            username="worker", password="password", position=self.position
        )

    def test_worker_str(self):
        self.assertEqual(str(self.worker), "worker: worker worker")


class TaskModelTest(TestCase):
    def setUp(self):
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
        self.task.tags.add(self.tag)

    def test_task_str(self):
        self.assertEqual(str(self.task), "Fix Bug")

    def test_task_clean(self):
        self.task.deadline = timezone.now().date() - timezone.timedelta(days=1)
        with self.assertRaises(ValidationError):
            self.task.clean()
