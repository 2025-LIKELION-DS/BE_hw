from django.urls import path
from .views import *
# *표시는 views에 있는 list, create, detail, update 등등을 모두 포함함

app_name = 'phone'

urlpatterns = [
    path('',IndexView.as_view(), name='list'),
    path('create/', create, name='create'),
    path('result/', result, name='result'),
    path('delete/<int:id>/', delete, name='delete'),
    path('update/<int:id>/', update, name='update'),
    path('detail/<int:id>/', detail, name='detail'),
]
