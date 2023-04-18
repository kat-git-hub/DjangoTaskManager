import django_tables2 as tables
from tasks.models import Task
from django.utils.translation import gettext as _


class TaskTable(tables.Table):
    TEMPLATE = '''
   <a href="{% url 'tasks:update' record.pk %}" class="tbl_icon edit">{{ edit }}</a>
   <a href="{% url 'tasks:delete' record.pk %}" class="tbl_icon delete">{{ delete }}</a>
'''
    created_at = tables.DateTimeColumn(accessor='date_joined')
    # links = tables.TemplateColumn(TEMPLATE, verbose_name='',
    #                               extra_context={'edit': _('Edit'), 'delete': _('Delete')})
    author = tables.Column(accessor='full_name', verbose_name=_('Full name'))


    class Meta:
        model = Task
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'username', 'status', 'author', 'created_at')