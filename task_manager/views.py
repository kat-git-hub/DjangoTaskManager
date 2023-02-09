from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.forms import AuthenticationForm
from django.urls.base import reverse_lazy


def index(request):
    return render(request, 'index.html',)


# class LoginUser(LoginView):
#     form_class = AuthenticationForm
#     template_name = 'users/login.html'
#     redirect_field_name = 'redirect_to'
#     next_page = reverse_lazy('index.html')


# class LogoutUser(LogoutView):
#     def get_next_page(self):
#         return reverse_lazy('index')
