from accounts.models import CustomUser
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from task.forms import CreateTaskForm
from .models import Task


class TasksListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task/task.html'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        base_queryset = Task.objects.all()
        search_query = self.request.GET.get('q', None)
        priority = self.request.GET.get('priority', None)
        date_sort = self.request.GET.get('date_sort', None)

        if search_query:
            self.queryset = base_queryset.filter(title__icontains=search_query)

        elif priority:
            self.queryset = base_queryset.filter(priority=priority)

        elif date_sort:
            if date_sort == 'ascending':
                self.queryset = base_queryset.order_by("due_date")
            elif date_sort == 'descending':
                self.queryset = base_queryset.order_by("-due_date")
        else:
            self.queryset = base_queryset
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        employees = CustomUser.objects.all()
        
        completed_tasks = self.queryset.filter(status='Completed')
        inprogress_tasks = self.queryset.filter(status='In_Progress')
        overdue_tasks = self.queryset.filter(status='Overdue')
        
        context['completed'] = completed_tasks
        context['inprogress'] = inprogress_tasks
        context['overdue'] = overdue_tasks
        context['employees'] = employees
        context['search_query'] = self.request.GET.get('q', '')
        
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task/task_detail.html'

  
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'task/create_task.html'
    success_url = reverse_lazy('tasks')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'task/update_task.html'
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Task updated successfully!')
        return response


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("tasks")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Task deleted successfully!')
        return response
