import django_filters as filters
from .models import Task
from labels.models import Labels


class TaskFilter(filters.FilterSet):
    
    show_my_tasks = filters.BooleanFilter(field_name='author', label = 'My tasks',
                                         method = 'filter_tasks')
    labels = filters.ModelChoiceFilter(queryset=Labels.objects.all(), label='Label')


    def filter_tasks(queryset, name, value):
        if value:
            user = queryset.model._meta.model_name.author_model().objects.filter(username=value).first()
            if user:
                return queryset.filter(author=user)
            else:
                return queryset.none()
        return queryset


    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'show_my_tasks']
        filter_overrides = {
             filters.BooleanFilter: {
                'filter_class': filters.BooleanFilter,
                 'extra': lambda f: {'widget': CheckboxInput,},
             },
         }
