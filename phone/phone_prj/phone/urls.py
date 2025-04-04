from django.urls import path
from .views import *
# *표시는 views에 있는 list, create, detail, update 등등을 모두 포함함

app_name = 'phone'

urlpatterns = [
    path('', list, name='list'),
    path('create/', create, name='create'),
    path('result/', result, name='result'),
    path('delete/<str:name>/', delete, name='delete'),
    path('update/<str:name>/', update, name='update'),
    path('detail/<str:name>/', detail, name='detail'),
]
