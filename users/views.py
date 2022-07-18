from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_tables2 import SingleTableView
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model
from users.models import User
from .tables import UserTable
from users.forms import UserForm
from django.views import generic


class CreateUser(generic.CreateView):
    queryset = User.objects.all()
    model = User
    template_name = 'create.html'
    form_class = UserForm
    #fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
    success_url = reverse_lazy('users')

# def register(response):
#     if response.method == "POST":

#         form = UserForm(response.POST)
#         if form.is_valid():
#             form.save()
#         return redirect("/users")
#     else:
#         form = UserForm()
#     return render(response, "register/register.html", {"form":form})


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'password')


class UserView(SingleTableView):
    model = User
    template_name = 'templates/users.html'
    table_class = UserTable

