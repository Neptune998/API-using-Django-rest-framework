from rest_framework import serializers
from .forms import LoginForm
from django.contrib.auth.models import User


# Custom Model serializer class
class LoginFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoginForm
        fields = "__all___"


# Build in User model serializer class
class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['id','username','email','password']



