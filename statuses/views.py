#from django.shortcuts import render
from .forms import StatusForm
from .tables import StatusesTable
from statuses.models import Status
from django.views import generic
from django.contrib import messages
from django.urls.base import reverse_lazy
from django_tables2 import SingleTableView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class StatusesView(SingleTableView):
    model = Status
    template_name = 'templates/statuses.html'
    table_class = StatusesTable
    extra_context = {'title': "Statuses"}


class CreateStatus(generic.CreateView):
    #queryset = Labels.objects.all()
    model = Status
    template_name = 'general_pattern.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses:statuses')
    extra_context = {'title': "Create status",}

    def form_valid(self, form):
        messages.success(self.request, 'Status created successfully.')
        return super().form_valid(form)


class UpdateStatus(LoginRequiredMixin, UpdateView):
    model = Status
    template_name = 'general_pattern.html' 
    extra_context = {'title': "Status Change"}
    form_class = StatusForm
    success_url = reverse_lazy('statuses:statuses')
    
   
    def form_valid(self, form):
        messages.success(self.request, 'Status updated.')
        return super().form_valid(form)



class DeleteStatus(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = "delete.html"
    extra_context = {'title': 'Delete status'}
    success_url = reverse_lazy('statuses:statuses')

    def form_valid(self, form):
        messages.success(self.request, 'Status deleted successfully.')
        return super().form_valid(form)