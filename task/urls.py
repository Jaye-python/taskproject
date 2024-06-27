from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.TasksListView.as_view(), name="tasks"),
    path('task/create/', views.TaskCreateView.as_view(), name='create-task'),
    path("task/update-task/<pk>/", views.TaskUpdateView.as_view(), name="update-task"),
    path("task/delete-task/<pk>/", views.TaskDeleteView.as_view(), name="delete-task"),
    path("task-detail/<pk>/", views.TaskDetailView.as_view(), name="task-detail"),
    # path('login/', views.user_login, name='login'),
    # path('signup/', views.user_signup, name='signup'),
    # path('logout/', views.user_logout, name='logout'),
    
]