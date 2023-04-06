from django.urls import path
from statuses import views


app_name = 'statuses'
urlpatterns = [
    path('', views.StatusesView.as_view(template_name='labels-statuses-template.html'), name='statuses'),
    path('create/', views.CreateStatus.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateStatus.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteStatus.as_view(), name='delete'),
   
]