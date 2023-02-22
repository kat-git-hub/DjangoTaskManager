from django.shortcuts import render
#from django.contrib.auth.views import LoginView, LogoutView
#from django.contrib.auth.forms import AuthenticationForm
#from django.urls.base import reverse_lazy
#from django.views import View
#from django.contrib import messages
#from django.contrib.auth import login, logout


def index(request):
    return render(request, 'index.html',)
