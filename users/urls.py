from venv import create
from django.urls import path
from users import views
#from .views import UserView, CreateUser


app_name = 'users'
urlpatterns = [
    path('', views.UserView.as_view(template_name='users.html')),
    path('create/', views.CreateUser.as_view(), name='users/create/'),
    #path('create/', views.CreateUser.as_view(), name='create_user'),
]


# app_name = 'films'

# urlpatterns = [
#     path('', views.FilmListView.as_view(), name='all'),
#     path('films/<int:pk>/detail', views.FilmDetailView.as_view(), name='film_detail'),
#     path('films/create/', views.FilmCreateView.as_view(), name='film_create'),
#     path('films/<int:pk>/update/', views.FilmUpdateView.as_view(), name='film_update'),
#     path('films/<int:pk>/delete/', views.FilmDeleteView.as_view(), name='film_delete'),
# ]