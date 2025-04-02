from django.urls import path
from .views import list, result

urlpatterns = [
    path('', list, name = 'list'),
    path('result/', result, name='result'),
]