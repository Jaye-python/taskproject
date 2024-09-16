from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_email
from django_prometheus.models import ExportModelOperationsMixin
# from accounts.forms import LoginForm, SignupForm


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, ):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password=None,):
        if not email:
            raise ValueError('Email is Required')
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


def default_id():
    return {
        "id": []
    }


class CustomUser(ExportModelOperationsMixin('customuser'), AbstractUser):
    username = None
    first_name = models.CharField(max_length=20)
    email = models.EmailField(db_index=True, unique=True, validators=[validate_email])
    profile_pix = models.ImageField(upload_to='profile_pics/')


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    EMAIL_FIELD = 'email'

    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return self.email