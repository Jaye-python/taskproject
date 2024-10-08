from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django_prometheus.models import ExportModelOperationsMixin


class Task(ExportModelOperationsMixin("task"), models.Model):
    STATUS_CHOICES = [
        ("In_Progress", "In_Progress"),
        ("Completed", "Completed"),
        ("Overdue", "Overdue"),
    ]

    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="In_Progress",
    )
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="Low",
    )
    due_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("task-detail", args=[self.id])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]
