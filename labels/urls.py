from django.urls import path
from labels import views


app_name = 'labels'
urlpatterns = [
    path('', views.LabelsView.as_view(template_name='labels-statuses-template.html'), name='labels'),
    path('create/', views.CreateLabel.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateLabel.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteLabel.as_view(), name='delete'),
   
]