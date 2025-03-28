from django.contrib import admin
from django.urls import path
from password import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('password_generator/',views.password_generator,name='result'),
    path('error1/',views.error1,name='error1'),
    path('error2/',views.error2,name='error2'),
    path('error3/',views.error3,name='error3'),
]
