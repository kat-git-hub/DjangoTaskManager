from tasks.models import Task
from tasks.forms import TaskForm
from tasks.tables import TaskTable
from tasks.filter import TaskFilter
from django.contrib import messages
from django.urls.base import reverse_lazy
from django_tables2 import SingleTableView
from django_filters.views import FilterView
from django.utils.translation import gettext as _
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView


class TasksView(LoginRequiredMixin, FilterView, SingleTableView):
    model = Task
    filterset_class = TaskFilter
    table_class = TaskTable
    extra_context = {'title': _('Tasks')}


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_view.html'
    extra_context = {'title': _('Task view')}


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'general_pattern.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:tasks')
    extra_context = {'title': _('Tasks')}

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, _('Task created successfully'))
        return super().form_valid(form)


class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'general_pattern.html'
    extra_context = {'title': _('Changing task')}
    form_class = TaskForm
    success_url = reverse_lazy('tasks:tasks')

    def form_valid(self, form):
        messages.success(self.request, _('Task updated'))
        return super().form_valid(form)


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "delete.html"
    extra_context = {'title': _('Delete task')}
    success_url = reverse_lazy('tasks:tasks')

    def form_valid(self, form):
        if self.request.user == self.get_object().author:
            messages.success(self.request, _('Task deleted successfully'))
            return super().form_valid(form)
        else:
            form.add_error(None, _('Task can be deleted only by the owner'))
            return self.form_invalid(form)
