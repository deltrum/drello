from django.shortcuts import render

# RestFramewok
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response

# Custom
from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
def TaskColumns(request):
    try:
        task_columns = TaskColumn.objects.all()
    except TaskColumn.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers = TaskColumnSerializer(task_columns, many=True)
        return Response(serializers.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Tasks(request, pk):
    token = request.META['HTTP_AUTHORIZATION'].replace("token", "").replace(" ", "")
    user = Token.objects.get(key=token).user

    try:
        tasks = Task.objects.filter(owner = user.id).filter(attachment = pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers = TaskSerializer(tasks, many=True)
        return Response(serializers.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def AddTask(request):
    token = request.META['HTTP_AUTHORIZATION'].replace("token", "").replace(" ", "")
    user = Token.objects.get(key=token).user

    task = Task(owner = user)
    if request.method == "POST":
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def DeleteTask(request, pk):
    try:
        task = Task.objects.get(id = pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        task.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def ChangeColumnTask(request, pk):
    try:
        task = Task.objects.get(id = pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)