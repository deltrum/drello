from django.shortcuts import render

# RestFramewok
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Custom
from .serializers import *

@api_view(['POST'])
def Register(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "successfully registered a new user!"
        else:
            data = serializer.errors
        return Response(data)