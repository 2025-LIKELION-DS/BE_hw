from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)

#python manage.py createsuperuser(admin 생성)
#유수빈/suebenny2@naver.com/1234