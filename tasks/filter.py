from .models import Task
from labels.models import Labels
import django_filters as filters
from django.forms.widgets import CheckboxInput
from django.utils.translation import gettext as _


class TaskFilter(filters.FilterSet):
    show_my_tasks = filters.BooleanFilter(field_name='author', label=_('My tasks'),
                                          method='filter_tasks', widget=CheckboxInput)
    labels = filters.ModelChoiceFilter(queryset=Labels.objects.all(), label=_('Label'))

    def filter_tasks(self, queryset, name, value):
        if value and self.request.user.is_authenticated:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'show_my_tasks']
        filter_overrides = {filters.BooleanFilter: {
                            'filter_class': filters.BooleanFilter,
                            'extra': lambda f: {'widget': CheckboxInput, },
                            },
                            }
