from django.urls import path
from tasks import views


app_name = 'tasks'
urlpatterns = [
    path('', views.TasksView.as_view(template_name='tasks.html'), name='tasks'),
    path('create/', views.CreateTask.as_view(), name='create'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='view_task'),
    path('<int:pk>/update/', views.UpdateTask.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteTask.as_view(), name='delete'),

]
