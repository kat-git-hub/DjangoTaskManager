from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_tables2 import SingleTableView
from users.models import User
from .tables import UserTable
from users.forms import UserForm
from django.views import generic, View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView



class CreateUser(generic.CreateView):
    queryset = User.objects.all()
    model = User
    template_name = 'general_pattern.html'
    form_class = UserForm
    success_url = reverse_lazy('login')
    extra_context = {'title': "Registretion"}

    def form_valid(self, form):
        messages.success(self.request, 'User account created successfully.')
        return super().form_valid(form)


class UserView(SingleTableView):
    model = User
    template_name = 'templates/users.html'
    table_class = UserTable


class UpdateUser(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'general_pattern.html' 
    form_class = UserForm
    success_url = reverse_lazy('login')
    extra_context = {'title': "User Change"}
   
    def form_valid(self, form):
        messages.success(self.request, 'User updated.')
        return super().form_valid(form)

    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'User Change'
    #     return context

# -------------------------------#####
class LoginView(View):
    template_name = 'general_pattern.html'
    extra_context = {'title': "Entrance"}
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


