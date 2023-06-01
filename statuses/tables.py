import django_tables2 as tables
from statuses.models import Status
from django.utils.translation import gettext as _


class StatusesTable(tables.Table):
    TEMPLATE = '''
   <a href="{% url 'statuses:update' record.pk %}" class="tbl_icon edit">{{ edit }}</a>
   <a href="{% url 'statuses:delete' record.pk %}" class="tbl_icon delete">{{ delete }}</a>
'''
    links = tables.TemplateColumn(TEMPLATE, verbose_name='',
                                  extra_context={'edit': _('Edit'), 'delete': _('Delete')})
    name = tables.Column(accessor='name', verbose_name=_('Name'))

    class Meta:
        model = Status
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'name', 'created_at', 'links')
        attrs = {
            'class': 'table table-hover'
        }
