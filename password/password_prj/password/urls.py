from django.contrib import admin
from django.urls import path
from . import views

app_name = 'password'
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index, name = 'index'),
    path('result/', views.password_generator, name='password_generator'),

]