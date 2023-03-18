#from django.shortcuts import render


from .forms import LabelForm
from .tables import LabelsTable
from labels.models import Labels
from django.views import generic
from django.contrib import messages
from django.urls.base import reverse_lazy
from django_tables2 import SingleTableView

class LabelsView(SingleTableView):
    model = Labels
    template_name = 'templates/labels.html'
    table_class = LabelsTable
    extra_context = {'title': "Labels"}


class CreateLabel(generic.CreateView):
    queryset = Labels.objects.all()
    model = Labels
    template_name = 'general_pattern.html'
    form_class = LabelForm
    success_url = reverse_lazy('labels:labels')
    extra_context = {'title': "Create label",}

    def form_valid(self, form):
        messages.success(self.request, 'Label created successfully.')
        return super().form_valid(form)


