#from re import template
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_tables2 import SingleTableView
from users.models import User
from .tables import UserTable
from users.forms import UserForm
from django.views import generic, View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages



class CreateUser(generic.CreateView):
    queryset = User.objects.all()
    model = User
    template_name = 'create.html'
    form_class = UserForm
    success_url = reverse_lazy('login')
    # + add success_message
    #success_message = messages.add_message(request, messages.SUCCESS, "Registration Was Successfull")
 


class UserView(SingleTableView):
    model = User
    template_name = 'templates/users.html'
    table_class = UserTable



class LoginView(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('/')
        return render(request, self.template_name, {'form': form})

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')



# def logout_view(request):
#     logout(request)
#     return redirect('/')


# def login_view(request):

#     context = {}

#     user = request.user
#     if user.is_authenticated: 
#         return redirect("home")

#     if request.POST:
#         form = AccountAuthenticationForm(request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)
#                 messages.add_message(request, messages.SUCCESS, "You are login")
#                 return redirect("/")

#     else:
#         form = AccountAuthenticationForm()

#     context['login_form'] = form
    
#     return render(request, "login.html", context)

