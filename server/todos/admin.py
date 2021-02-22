from django.contrib import admin

# Custom
from .models import *


# Register your models here.

admin.site.register(TaskColumn)
admin.site.register(Task)
