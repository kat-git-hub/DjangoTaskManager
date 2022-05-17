from venv import create
from django.urls import path
from .views import UserView, CreateUser


urlpatterns = [
    path('', UserView.as_view(template_name='users.html')),
    #path('create/', CreateUser.as_view(), name='create_user'),
]


# from django.urls import path

# from . import views

# app_name = 'polls'
# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     ...
# ]