from django.contrib import admin

from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)

#admin 계정: admin/1234