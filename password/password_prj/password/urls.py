from django.urls import path
from .views import *

app_name='password'

urlpatterns=[
    path('error1/', error1, name='error1'),
    path('error2/', error2, name='error2'),
    path('error3/', error3, name='error3'),
    path('', index, name='index'),
    path('result/', password_generator, name='password_generator')
]