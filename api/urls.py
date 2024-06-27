from django.urls import path
from .views import AjaxTasksView, InProgressTasksView, CompletedTasksView, OverdueTasksView, SearchTaskView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('tasks/in_progress/', InProgressTasksView.as_view(), name='in_progress_tasks'),
    path('tasks/completed/', CompletedTasksView.as_view(), name='completed_tasks'),
    path('tasks/overdue/', OverdueTasksView.as_view(), name='overdue_tasks'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('ajax/tasks/', AjaxTasksView.as_view(), name='ajax-tasks'),
    path('task/search/', SearchTaskView.as_view(), name='task-search'),    
    
    
]