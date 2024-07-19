from django.test import TestCase, Client
from django.urls import reverse
from manager.models import Position, TaskType, Tag, Worker, Task


class ViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
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

    def test_home_view(self):
        self.client.login(username="worker", password="password")
        response = self.client.get(reverse("manager:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/home.html")

    def test_position_list_view(self):
        self.client.login(username="worker", password="password")
        response = self.client.get(reverse("manager:position-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/position_list.html")

    def test_tasktype_list_view(self):
        self.client.login(username="worker", password="password")
        response = self.client.get(reverse("manager:tasktype-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/tasktype_list.html")

    def test_worker_list_view(self):
        self.client.login(username="worker", password="password")
        response = self.client.get(reverse("manager:worker-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/worker_list.html")

    def test_worker_detail_view(self):
        self.client.login(username="worker", password="password")
        response = self.client.get(
            reverse("manager:worker-detail", args=[self.worker.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/worker_detail.html")

    def test_task_list_view(self):
        self.client.login(username="worker", password="password")
        response = self.client.get(reverse("manager:task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/task_list.html")

    def test_task_detail_view(self):
        self.client.login(username="worker", password="password")
        response = self.client.get(reverse(
            "manager:task-detail", args=[self.task.id]
        ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/task_detail.html")

    def test_tag_list_view(self):
        self.client.login(username="worker", password="password")
        response = self.client.get(reverse("manager:tag-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/tag_list.html")
