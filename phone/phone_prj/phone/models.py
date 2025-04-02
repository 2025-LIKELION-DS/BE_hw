from django.db import models

# Create your models here.
class Phone(models.Model):
    name=models.CharField(max_length=10) # 이름 
    phone_num=models.CharField(max_length=11) # 전화번호
    email=models.EmailField(null=False, unique=True, blank=False)
    create_at=models.DateField(auto_now_add=True)

    def __str__(self): # 전화번호 list - 이름으로 목록 나타내기
        return self.name