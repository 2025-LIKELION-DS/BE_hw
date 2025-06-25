from django.db import models
from users.models import User
import os
from uuid import uuid4
from django.utils import timezone

def upload_filepath(instance,filename):
    today_str=timezone.now().strftime("%Y%m%d")
    file_basename=os.path.basename(filename)
    return f'{instance._meta.model_name}/{today_str}/{str(uuid4())}_{file_basename}'


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    author=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="posts")
    is_anonymouse=models.BooleanField(default=False) # 익명 여부
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    category=models.ManyToManyField(to=Category,through="PostCategory",related_name="category_posts")
    like=models.ManyToManyField(to=User,through="Like",related_name="liked_posts")
    scrap=models.ManyToManyField(to=User,through="Scrap",related_name="scraped_posts")
    image=models.ImageField(upload_to=upload_filepath,blank=True)
    video=models.FileField(upload_to=upload_filepath,blank=True)

    def __str__(self):
        return f'[{self.id}]{self.title}'

    @property
    def anonymouse(self):
        if self.is_anonymouse: # 익명일 경우
            return "익명"
        else: # 익명 아닐 경우
            return self.author.nickname

class PostCategory(models.Model): # 새로운 필드 추가 없기에 따로 생성할 필요는 x
    category=models.ForeignKey(to=Category,on_delete=models.CASCADE,related_name='categories_postcategory')
    post=models.ForeignKey(to=Post,on_delete=models.CASCADE,related_name='posts_postcategory')


class Comment(models.Model):
    post=models.ForeignKey(to=Post,on_delete=models.CASCADE,related_name="comments")
    content=models.TextField()
    author=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="comments")
    is_anonymouse=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.id}]{self.content}'

    @property
    def anonymouse(self):
        if self.is_anonymouse: # 익명일 경우
            return "익명"
        else: # 익명 아닐 경우
            return self.author.nickname

class Like(models.Model): # 중간테이블
    post=models.ForeignKey(to=Post,on_delete=models.CASCADE,related_name="likes")
    user=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="likes")

class Scrap(models.Model):
    post=models.ForeignKey(to=Post,on_delete=models.CASCADE,related_name="scraps")
    user=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="scraps")



    
