from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    university = models.CharField(max_length=50,blank=False, null=False)
    email  = models.CharField(max_length=30, unique=True , blank=False, null=False)
    nickname = models.CharField(max_length=20, unique=True )
