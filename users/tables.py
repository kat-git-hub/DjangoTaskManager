import django_tables2 as tables
from users.models import User
from django.utils.translation import gettext as _


class UserTable(tables.Table):
    TEMPLATE = '''
   <a href="{% url 'users:update' record.pk %}" class="tbl_icon edit">{{ edit }}</a>
   <a href="{% url 'users:delete' record.pk %}" class="tbl_icon delete">{{ delete }}</a>
'''
    created_at = tables.DateTimeColumn(accessor='date_joined')
    links = tables.TemplateColumn(TEMPLATE, verbose_name='',
                                  extra_context={'edit': _('Edit'), 'delete': _('Delete')})
    full_name = tables.Column(accessor='full_name', verbose_name=_('Full name'))


    class Meta:
        model = User
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'username', 'full_name', 'created_at', 'links')