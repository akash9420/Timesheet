from math import trunc

from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,BaseUserManager
from sympy.codegen.cxxnodes import using


# Create your models here.

class UserManagaer(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError("User Must have email address")
        if not username:
            raise ValueError("User Must have username")
        user = self.model(
            email = self.normalize_email(email),
            first_name =first_name,
            last_name = last_name,
            username=username,
            password=password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,username,email,password=None):
        user = self.create_user(
            first_name=first_name,
            last_name= last_name,
            email= self.normalize_email(email),
            password=password,
            username=username
        )
        user.is_active=True,
        user.is_staff=True,
        user.is_superuser=True
        user.is_admin=True
        user.save(using=self._db)
        return user



class User(AbstractUser):
    pass