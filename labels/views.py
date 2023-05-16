from .forms import LabelForm
from .tables import LabelsTable
from labels.models import Labels
from django.views import generic
from django.contrib import messages
from django.urls.base import reverse_lazy
from django_tables2 import SingleTableView
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView


class LabelsView(LoginRequiredMixin, SingleTableView):
    model = Labels
    template_name = 'templates/labels_statuses.html'
    table_class = LabelsTable
    extra_context = {'title': _('Labels'), 'page_type': 'labels'}


class CreateLabel(LoginRequiredMixin, generic.CreateView):
    model = Labels
    template_name = 'general_pattern.html'
    form_class = LabelForm
    success_url = reverse_lazy('labels:labels')
    extra_context = {'title': _('Create label'), }

    def form_valid(self, form):
        messages.success(self.request, _('Label created successfully'))
        return super().form_valid(form)


class UpdateLabel(LoginRequiredMixin, UpdateView):
    model = Labels
    template_name = 'general_pattern.html'
    extra_context = {'title': _('Label change')}
    form_class = LabelForm
    success_url = reverse_lazy('labels:labels')

    def form_valid(self, form):
        messages.success(self.request, _('Label updated'))
        return super().form_valid(form)


class DeleteLabel(LoginRequiredMixin, DeleteView):
    model = Labels
    template_name = "delete.html"
    extra_context = {'title': _('Delete label')}
    success_url = reverse_lazy('labels:labels')

    def form_valid(self, form):
        messages.success(self.request, _('Label deleted successfully'))
        return super().form_valid(form)
