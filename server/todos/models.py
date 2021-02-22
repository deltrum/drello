from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from colorfield.fields import ColorField

# Create your models here.
class TaskColumn(models.Model):
    title = models.CharField(max_length=100)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.title


class Task(models.Model):
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now, blank=True)
    attachment = models.ForeignKey(TaskColumn, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.content
