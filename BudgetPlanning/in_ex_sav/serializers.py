from rest_framework import serializers
from .models import Savings, Income, Expence

class SavingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savings
        fields = ['id','savings_name']



class SavingsDetailDeleteSerializer(serializers.Serializer):
    savings_id = serializers.IntegerField()

    

class ExpenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expence
        fields = ['id','expence_name']


class ExpenceDetailDeleteSerializer(serializers.Serializer):
    expences_id = serializers.IntegerField()

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id','income_name']

class IncomeDetailDeleteSerializer(serializers.Serializer):
    income_id = serializers.IntegerField()