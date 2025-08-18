from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser
from rest_framework.authtoken.models import Token, Token.objects.create, get_user_model().objects.create_user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "bio", "profile_picture", "followers"]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 
    #adding new custom field 

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    #creating new custom fields to be serialized

    def validate(self, data):
        user = authenticate(**data) #authenticate is imported func
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")
