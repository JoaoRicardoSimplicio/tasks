from typing import Optional

from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class Task(models.Model):

    TaskStatus = models.TextChoices("TaskStatus", "Todo Done")

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    status = models.CharField(blank=False, max_length=15, choices=TaskStatus, default="Todo")

    @classmethod
    def get_or_none(cls, pk: int) -> Optional['Task']:
        try:
            return Task.objects.get(id=pk)
        except ObjectDoesNotExist:
            return None

    def __str__(self):
        return self.title
