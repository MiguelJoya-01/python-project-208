from django.conf import settings
from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.ForeignKey(
        'statuses.Status',
        on_delete=models.PROTECT,
        related_name='tasks',
    )
    executor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='assigned_tasks',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='created_tasks',
    )
    labels = models.ManyToManyField(
        Label,
        blank=True,
        related_name='tasks',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
