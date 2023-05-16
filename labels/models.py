from django.db import models
from django.utils.translation import gettext as _


class Labels(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('Created date'))

    def __str__(self):
        return self.name
