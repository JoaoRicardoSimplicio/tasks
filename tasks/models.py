from django.db import models


class Task(models.Model):

    TaskStatus = models.TextChoices("TaskStatus", "Todo Done Skipped Canceled")

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    status = models.CharField(blank=False, max_length=15, choices=TaskStatus, default="Todo")

    def __str__(self):
        return self.title
