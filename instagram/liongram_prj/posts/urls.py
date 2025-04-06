from django.urls import path
from .views import *
# *표시는 views에 있는 list, create, detail, update 등등을 모두 포함함

app_name = 'posts'

urlpatterns = [
    path('', list, name='list'),
    path('create/',create,name='create'),
    path('detail/<int:id>',detail,name='detail'),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),
    path('result/',result,name='result'),
    
]
