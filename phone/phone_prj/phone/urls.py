from django.urls import path
from .views import *

app_name = 'phone'

urlpatterns = [
    path('', ListView.as_view(), name = 'list'),
    path('create/',create,name='create'),
    path('detail/<int:id>/',detail,name='detail'),
    path('delete/<int:id>/',delete,name='delete'),
    path('update/<int:id>/',update,name='update'),
    path('result/', result, name = 'result'),
]