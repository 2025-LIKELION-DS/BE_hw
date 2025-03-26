from django.contrib import admin
from django.urls import path
from wordcount import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('word-count/', views.word_count, name='word_count'),
    path('result/', views.result,name='result'),
    path('hello/',views.hello,name='hello'),
]
