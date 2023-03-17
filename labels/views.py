#from django.shortcuts import render


from .forms import LabelForm
from .tables import LabelsTable
from labels.models import Labels
from django.views import generic
from django_tables2 import SingleTableView

class LabelsView(SingleTableView):
    model = Labels
    template_name = 'templates/labels.html'
    table_class = LabelsTable


class CreateLabel(generic.CreateView):
    queryset = Labels.objects.all()
    model = Labels
    template_name = 'users/general_pattern.html'
    form_class = LabelForm
    #success_url = reverse_lazy('login')
    extra_context = {'title': "Create label", 'button': "Create"}


