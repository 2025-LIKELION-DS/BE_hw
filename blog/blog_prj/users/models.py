from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email=models.CharField(max_length=30, unique=True, null=False, blank=False) 
    # 중복 방지, null 비허용, 빈칸 비허용
    nickname=models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.username