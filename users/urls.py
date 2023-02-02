from venv import create
from django.urls import path
from users import views


app_name = 'users'
urlpatterns = [
    path('', views.UserView.as_view(template_name='users.html')),
    path('create/', views.CreateUser.as_view(), name='users/create/'),
]