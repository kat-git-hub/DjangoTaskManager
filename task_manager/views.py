from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.utils.translation import gettext as _
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request, 'index.html',)


class LoginView(View):
    template_name = 'general_pattern.html'
    extra_context = {'title': _('Entrance')}

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, self.template_name,
                      {'form': form, **self.extra_context})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, _('You have successfully logged in'))
            return redirect('main')
        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, _('You are logged out'))
        return redirect('main')
