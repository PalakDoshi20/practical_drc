# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.


class UserManager(BaseUserManager):
    def _create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("User must have a username")
        if not username:
            raise ValueError("User must have a password")
        user = self.model(
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        return self._create_user(username, password, **extra_fields)

class User(AbstractBaseUser):
  username = models.CharField(max_length=50, unique=True)
  email = models.EmailField(max_length=100, unique=True)
  password = models.CharField(max_length=20)
  mobile = models.CharField(max_length=10, unique=True)
  otp = models.IntegerField(default=0000)
  login_counter = models.IntegerField(default=0)

  USERNAME_FIELD = "username"

  objects = UserManager()

  def __str__(self):
      return self.username
