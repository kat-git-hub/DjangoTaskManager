import django_tables2 as tables
from labels.models import Labels
from django.utils.translation import gettext as _


class LabelsTable(tables.Table):
    TEMPLATE = '''
   <a href="{% url 'labels:update' record.pk %}" class="tbl_icon edit">{{ edit }}</a>
   <a href="{% url 'labels:delete' record.pk %}" class="tbl_icon delete">{{ delete }}</a>
''' # noqa: E501
    links = tables.TemplateColumn(TEMPLATE, verbose_name='',
                                  extra_context={'edit': _('Edit'),
                                                 'delete': _('Delete')})
    name = tables.Column(accessor='name', verbose_name=_('Name'))

    class Meta:
        model = Labels
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'name', 'created_at', 'links')
