import django_tables2 as tables
from tasks.models import Task
from django.utils.translation import gettext as _


class TaskTable(tables.Table):
    TEMPLATE = '''
   <a href="{% url 'tasks:update' record.pk %}" class="tbl_icon edit">{{ edit }}</a>
   <a href="{% url 'tasks:delete' record.pk %}" class="tbl_icon delete">{{ delete }}</a>
'''

    links = tables.TemplateColumn(TEMPLATE, verbose_name='',
                                  extra_context={'edit': _('Edit'), 'delete': _('Delete')})
    name = tables.TemplateColumn('<a href="{% url "tasks:view_task" record.pk %}">{{ record.name }}</a>')


    class Meta:
        model = Task
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'name', 'status', 'author', 'executor', 'created_at', 'links')