from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)

#python manage.py createsuperuser(admin 생성)
#유수빈/suebenny2@naver.com/1234