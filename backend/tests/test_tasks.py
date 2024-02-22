from datetime import timedelta

from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse


from tasks.models import Task


class TasksTestCase(TestCase):
    def setUp(self):
        Task.objects.create(
            title="This is task number 1",
            due_date=timezone.now() + timedelta(days=1),
        )
        Task.objects.create(
            title="This is task number 2",
            due_date=timezone.now() - timedelta(days=2),
        )

    def test_tasks_can_be_counted(self):
        """Make sure we can query tasks and get their count"""
        count = Task.objects.count()

        self.assertGreater(count, 0, "Failed, count is not greather than 0")
        self.assertEqual(2, count)

    def test_can_create_task_via_post(self):
        """Can create task via post"""
        client = Client()
        title = "Task created via test"
        response = client.post(
            reverse("add_task"),
            {
                "title": title,
                "done": True,
                "due_date": timezone.now() - timedelta(days=3),
            },
        )

        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse("index"))
        self.assertContains(response, title)
