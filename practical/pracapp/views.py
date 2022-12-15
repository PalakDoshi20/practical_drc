# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import socket
from collections import defaultdict
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterUserSerializer, LoginViewSerializer, OtpVerifySerializer
from rest_framework import status
from .models import User
from django.shortcuts import render
import math, random
import datetime
from collections import defaultdict


# Create your views here.
def send_otp_mobile(mobile):
  digits = "0123456789"
  OTP = ""

  for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]

  return OTP


class RegisterApi(APIView):
  

  def post(self, request, *args, **kwargs):
    print("request======================", request)
    serializer = RegisterUserSerializer(data=request.data)
    
    if serializer.is_valid():
      serializer.save()
      # usename = User.objects.get(username=request.data.get('username'))
      # # user = User.objects.get(id=usename.id)
      # if request.data.get('mobile'):
      #   otp = send_otp_mobile(request.data.get('mobile'))
      #   usename.otp = otp
      #   usename.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
  def post(self, request):
    serializer = LoginViewSerializer(data=request.data)
    if serializer.is_valid():
      usename = User.objects.get(mobile=request.data.get('mobile'))
      otp = send_otp_mobile(request.data.get('mobile'))
      usename.otp = otp
      usename.save()
      return Response({'message': "Otp send to request number"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyUserOtp(APIView):

  def post(self, request, pk):
    username = User.objects.get(id=pk)
    # if not datetime.now() - request.session['last_login'] > datetime.timedelta(0, 5 * 60, 0):
    serializer =  OtpVerifySerializer(data=request.data)
    if serializer.is_valid():
      requestotp = request.data.get('otp')
      if username.login_counter < 3 and str(username.otp) == requestotp:
        username.login_counter = 0
        username.save()
        return Response({'message': "Verify otp successfully"}, status=status.HTTP_200_OK)
      elif username.login_counter < 3 and str(username.otp) != requestotp:
        username.login_counter += 1
        username.save()
      else:
        return Response({'message': "You have reached the limit of login "}, status=status.HTTP_200_OK)
      return Response({'message': "Otp does not match, please enter valid otp "}, status=status.HTTP_400_BAD_REQUEST)
      # else :
      #   username.login_counter = 0
      #   username.save

