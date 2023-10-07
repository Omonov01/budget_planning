from rest_framework import serializers
from .models import CustomUser

class WhoAmISerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "telegram_id", "phone_number"]


class UserSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8, required=True, write_only=True,)


    class Meta:
        model = CustomUser
        fields = ["username", "password", "telegram_id", "phone_number"]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

        

class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8, required=True, write_only=True, style={'input_type': 'password'})
    
    class Meta:
        model = CustomUser
        fields = ["username", "password"]
        extra_kwargs = {'password': {'write_only': True}}

class UserLogOutSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8, required=True, write_only=True, style={'input_type': 'password'})
    
    class Meta:
        model = CustomUser
        fields = ["username", "password"]
        extra_kwargs = {'password': {'write_only': True}}
