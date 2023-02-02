#from re import template
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_tables2 import SingleTableView
#from django.views.generic.edit import CreateView
#from django.contrib.auth.views import LoginView
#from django.contrib.messages.views import SuccessMessageMixin
from users.models import User
from .tables import UserTable
from users.forms import UserForm
from django.views import generic
from django.contrib.auth import login, authenticate, logout
from users.forms import  AccountAuthenticationForm


class CreateUser(generic.CreateView):
    queryset = User.objects.all()
    model = User
    template_name = 'create.html'
    form_class = UserForm
    #success_url = reverse_lazy('login')
    # + add success_message

# def register(response):
#     if response.method == "POST":

#         form = UserForm(response.POST)
#         if form.is_valid():
#             form.save()
#         return redirect("/users")
#     else:
#         form = UserForm()
#     return render(response, "register/register.html", {"form":form})

#------
# don remember what is this
#-------
# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')


class UserView(SingleTableView):
    model = User
    template_name = 'templates/users.html'
    table_class = UserTable


def logout_view(request):
	logout(request)
	return redirect('/')


def login_view(request):

	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)

			if user:
				login(request, user)
				return redirect("home")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form
	return render(request, "login.html", context)