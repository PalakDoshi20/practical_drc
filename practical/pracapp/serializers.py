from rest_framework import serializers
from .models import User

class RegisterUserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ['username', 'email', 'mobile', 'password']


class LoginViewSerializer(serializers.Serializer):

  mobile = serializers.CharField(max_length=10)


class OtpVerifySerializer(serializers.Serializer):

  otp = serializers.IntegerField()
