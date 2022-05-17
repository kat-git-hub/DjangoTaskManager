#from django.shortcuts import render
#from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_tables2 import SingleTableView
from django.contrib.auth import get_user_model
from users.models import User
from .tables import UserTable


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'password')


class UserView(SingleTableView):
    model = User
    template_name = 'templates/users.html'
    table_class = UserTable

