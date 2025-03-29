from django.urls import path
from .views import *

app_name='password'

urlpatterns=[
    path('', index, name='index'),
    path('result/', password_generator, name='result'),
    path('error1/', error1, name='error1'),
]