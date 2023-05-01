from tasks.models import Task
from tasks.forms import TaskForm
from tasks.tables import TaskTable
from tasks.filter import TaskFilter
from django.views import generic
from django.contrib import messages
from django.urls.base import reverse_lazy
from django_tables2 import SingleTableView
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView


class TaskView(FilterView, SingleTableView):
    model = Task
    #template_name = 'templates/tasks.html'
    filterset_class = TaskFilter
    table_class = TaskTable


class CreateTask(generic.CreateView):
    #queryset = User.objects.all()
    model = Task
    template_name = 'general_pattern.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:tasks')
    extra_context = {'title': "Tasks"}

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Task created successfully.')
        return super().form_valid(form)


class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'general_pattern.html' 
    extra_context = {'title': "Changing task"}
    form_class = TaskForm
    success_url = reverse_lazy('tasks:tasks')
    
   
    def form_valid(self, form):
        messages.success(self.request, 'Task updated.')
        return super().form_valid(form)


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "delete.html"
    extra_context = {'title': 'Delete task'}
    success_url = reverse_lazy('tasks:tasks')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        # Check if the user is trying to delete their own profile
        if self.request.user == self.get_object().author:
            # Call the delete() method to delete the user object
            return self.delete(request, *args, **kwargs)
        else:
            # If the user is trying to delete someone else's profile, return a form error
            form = self.get_form()
            form.add_error(None, "Task can delete only owner.")
            return self.form_invalid(form)
