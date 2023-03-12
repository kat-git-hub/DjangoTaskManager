from django.urls import path
from users import views


app_name = 'users'
urlpatterns = [
    path('', views.UserView.as_view(template_name='users.html'), name='users'),
    path('create/', views.CreateUser.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateUser.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteUser.as_view(), name='delete'),
   
]