from rest_framework import serializers

# Custom
from .models import *

# Searializers here

class TaskColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskColumn
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'content', 'attachment', 'owner']
