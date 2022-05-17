import django_tables2 as tables
from users.models import User
from django.utils.translation import gettext as _
#from django.utils.translation import gettext_lazy as _


class UserTable(tables.Table):
    # T1     = '<a href="###">Edit</a>'
    # T2     = '<a href="писать сюда ссылку">Delete</a>'
    # edit = tables.TemplateColumn(T1)
    # delete = tables.TemplateColumn(T2)
    TEMPLATE = '''
   <a href="##" class="tbl_icon edit">{{ edit }}</a>
   <a href="##" class="tbl_icon delete">{{ delete }}</a>
'''
    created_at = tables.DateTimeColumn(accessor='date_joined')
    links = tables.TemplateColumn(TEMPLATE, verbose_name='',
                                  extra_context={'edit': _('Edit'), 'delete': _('Delete')})
    full_name = tables.Column(accessor='full_name', verbose_name=_('Full name'))


    class Meta:
        model = User
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'username', 'full_name', 'created_at', 'links')