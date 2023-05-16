from users.models import User
from .tables import UserTable
from users.forms import UserForm
from django.contrib import messages
from django.views import generic
from django.urls.base import reverse_lazy
from django_tables2 import SingleTableView
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView


class CreateUser(generic.CreateView):
    queryset = User.objects.all()
    model = User
    template_name = 'general_pattern.html'
    form_class = UserForm
    success_url = reverse_lazy('login')
    extra_context = {'title': _('Registration')}

    def form_valid(self, form):
        messages.success(self.request, _('User account created successfully'))
        return super().form_valid(form)


class UserView(SingleTableView):
    model = User
    template_name = 'templates/users.html'
    table_class = UserTable


class UpdateUser(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'general_pattern.html'
    extra_context = {'title': _('User Change')}
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, _('User updated'))
        return super().form_valid(form)


class DeleteUser(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "delete.html"
    extra_context = {'title': _('Delete user')}
    success_url = reverse_lazy('users:users')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object == request.user:
            return self.delete(request, *args, **kwargs)
        else:
            form = self.get_form()
            form.add_error(None, _('You are not allowed to delete other users profiles'))
            return self.form_invalid(form)
