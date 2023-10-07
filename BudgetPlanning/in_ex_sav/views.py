### html filelarni render qilish
from django.shortcuts import render
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
from rest_framework import filters

from . import serializers
from .models import Savings, Income, Expence

class UserSavingCreateAPIView(generics.CreateAPIView):
    queryset = Savings
    serializer_class = serializers.SavingsSerializer

class UserSavingDeleteAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        user = request.user  
        incomes_to_delete = Savings.objects.filter(user=user)
        incomes_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class SavingsDetailDeleteView(APIView):
     def delete(self, request, savings_id, *args, **kwargs):
        # Check if the savings item exists and belongs to the authenticated user
        try:
            savings_item = Savings.objects.get(id=savings_id, user=request.user)
            savings_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Savings.DoesNotExist:
            return Response({'error': 'Savings item not found.'}, status=status.HTTP_404_NOT_FOUND)


class UserSavingLISTAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.SavingsSerializer
        
    def get_queryset(self):
        user = self.request.user
        return Savings.objects.filter(user=user)

class UserExpenceCreateAPIView(generics.CreateAPIView):
    queryset = Expence
    serializer_class = serializers.ExpenceSerializer

class UserExpenceDeleteAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        user = request.user  
        incomes_to_delete = Expence.objects.filter(user=user)
        incomes_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ExpenceDetailDeleteView(APIView):
    def delete(self, request, savings_id, *args, **kwargs):
        # Check if the savings item exists and belongs to the authenticated user
        try:
            savings_item = Savings.objects.get(id=savings_id, user=request.user)
            savings_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Savings.DoesNotExist:
            return Response({'error': 'Savings item not found.'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserExpenceLISTAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ExpenceSerializer

    def get_queryset(self):
        user = self.request.user
        return Expence.objects.filter(user=user)


class UserIncomeCreateAPIView(generics.CreateAPIView):
    queryset = Income
    serializer_class = serializers.IncomeSerializer

class UserIncomeDeleteAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        user = request.user  
        incomes_to_delete = Income.objects.filter(user=user)
        incomes_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class IncomeDetailDeleteView(APIView):
    def delete(self, request, savings_id, *args, **kwargs):
        # Check if the savings item exists and belongs to the authenticated user
        try:
            savings_item = Savings.objects.get(id=savings_id, user=request.user)
            savings_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Savings.DoesNotExist:
            return Response({'error': 'Savings item not found.'}, status=status.HTTP_404_NOT_FOUND)


class UserIncomeLISTAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = serializers.IncomeSerializer

    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(user=user)