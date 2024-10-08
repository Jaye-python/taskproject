from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Task


class TaskModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="testuser@test.com", password="testpassword"
        )

    def test_string_representation(self):
        task = Task(title="Sample Task", assigned_to=self.user, due_date=timezone.now())
        self.assertEqual(str(task), task.title)

    def test_default_status(self):
        task = Task.objects.create(
            title="Sample Task",
            description="This is a sample task.",
            due_date=timezone.now(),
            category="General",
            assigned_to=self.user,
        )
        self.assertEqual(task.status, "In_Progress")

    def test_default_priority(self):
        task = Task.objects.create(
            title="Sample Task",
            description="This is a sample task.",
            due_date=timezone.now(),
            category="General",
            assigned_to=self.user,
        )
        self.assertEqual(task.priority, "Low")

    def test_status_choices(self):
        task = Task.objects.create(
            title="Sample Task",
            description="This is a sample task.",
            due_date=timezone.now(),
            category="General",
            assigned_to=self.user,
            status="Completed",
        )
        self.assertEqual(task.status, "Completed")

        task.status = "Overdue"
        task.save()
        self.assertEqual(task.status, "Overdue")

    def test_priority_choices(self):
        task = Task.objects.create(
            title="Sample Task",
            description="This is a sample task.",
            due_date=timezone.now(),
            category="General",
            assigned_to=self.user,
            priority="High",
        )
        self.assertEqual(task.priority, "High")

        task.priority = "Medium"
        task.save()
        self.assertEqual(task.priority, "Medium")

    def test_get_absolute_url(self):
        task = Task.objects.create(
            title="Sample Task",
            description="This is a sample task.",
            due_date=timezone.now(),
            category="General",
            assigned_to=self.user,
        )
        self.assertEqual(
            task.get_absolute_url(), reverse("task-detail", args=[task.id])
        )

    def test_ordering(self):
        task1 = Task.objects.create(
            title="Sample Task 1",
            description="This is a sample task.",
            due_date=timezone.now(),
            category="General",
            assigned_to=self.user,
        )
        task2 = Task.objects.create(
            title="Sample Task 2",
            description="This is another sample task.",
            due_date=timezone.now(),
            category="General",
            assigned_to=self.user,
        )
        tasks = Task.objects.all()
        self.assertEqual(tasks[0], task2)
        self.assertEqual(tasks[1], task1)
