from django.db import models
from users.models import User
from statuses.models import Status
from django.utils.translation import gettext as _


class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    status =  models.ForeignKey(Status, null=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
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


    def __str__(self):
        return self.name
