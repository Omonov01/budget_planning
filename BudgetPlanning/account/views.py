from django.conf import settings
### html filelarni render qilish
from django.shortcuts import render
### userning kiritayotgan malumotlarini verifikatsiya qiladi
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
### user so'rovlarini tekshirish uchun ishlatiladi.
from django.middleware import csrf
from django.db.models import Q


###rest_framework kutubxonalri
from rest_framework import generics
from rest_framework import status, permissions
from rest_framework.exceptions import AuthenticationFailed

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import filters

from . import serializer
from . import models

# Create your views here.

class SignUpAPIView(APIView):   
    model = models.CustomUser
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializer.UserSignUpSerializer

    def post(self, request, *args, **kwargs):
        serializers = serializer.UserSignUpSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Logged in successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            

        
        
class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
