# views.py

from django.views.generic.base import TemplateView
from rest_framework import generics

from task.models import Task

from .serializers import TaskSerializer


class InProgressTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(status="In_Progress")


class CompletedTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(status="Completed")


class OverdueTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(status="Overdue")


class SearchTaskView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get("q", "")
        queryset = Task.objects.filter(title__icontains=search_query)
        return queryset


class AjaxTasksView(TemplateView):
    template_name = "api/ajax_task.html"


class SearchTasksTemplateView(TemplateView):
    template_name = "api/ajax_task.html"
