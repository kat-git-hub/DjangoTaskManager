#from django.shortcuts import render
from labels.models import Labels
from .tables import LabelsTable
from django_tables2 import SingleTableView

class LabelsView(SingleTableView):
    model = Labels
    template_name = 'templates/labels.html'
    table_class = LabelsTable



