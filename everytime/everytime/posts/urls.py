from django.urls import path,include
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', main , name='main'),
]
