from rest_framework import serializers
from django.contrib.auth.models import User
#from django.core.validators import 
from .models import Journal


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'
        read_only_fields=['user']


class UserSerializer(serializers.ModelSerializer):
    journals = JournalSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'journals']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate_username(self,value):
        if len(value) < 5:
            raise serializers.ValidationError("Username must be at least 5 characters")
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value
    

    def validate_password(self,value):
        if len(value) < 6:
            raise serializers.ValidationError("Password Must be at least 6 characters")
        return value
    
    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email Already exist use different email")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user