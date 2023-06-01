from django.db import models
from users.models import User
from statuses.models import Status
from labels.models import Labels
from django.utils.translation import gettext as _


class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    status = models.ForeignKey(Status, null=True, on_delete=models.PROTECT, verbose_name=_('Status'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Date joined'))
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='authored_tasks',
        verbose_name=_('Author'),)
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='tasks_assigned_to',
        verbose_name=_('Executor'),)
    labels = models.ManyToManyField(
        Labels,
        blank=True,
        verbose_name=_('Labels'),)

    def __str__(self):
        return self.name
