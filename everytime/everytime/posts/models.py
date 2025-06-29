from django.db import models
from users.models import User
from django.contrib.auth import get_user_model
import os
from uuid import uuid4
from django.utils import timezone

def upload_filepath(instance, filename):
    today_str = timezone.now().strftime("%Y%m%d")
    file_basename = os.path.basename(filename)
    return f'{instance._meta.model_name}/{today_str}/{str(uuid4())}_{file_basename}'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()          
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_anonymous = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, through="PostCategory", related_name="posts")
    like = models.ManyToManyField(User, through="Like", related_name="like_posts")
    scrap = models.ManyToManyField(User, through="Scrap", related_name="scrap_posts")
    image = models.ImageField(upload_to=upload_filepath, blank=True)
    video = models.FileField(upload_to=upload_filepath, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()         
    author = models.CharField(max_length=100) 
    anonymity = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

class PostCategory(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, related_name='categories_postcategory')
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='posts_postcategory')

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_likes")

class Scrap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_scraps")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_scraps")