from django.urls import path
from .views import *

app_name = "posts"

urlpatterns = [
    path('', main, name='main'),
    path('update/<int:id>/', update, name='update'),    
    path('detail/<int:id>/', detail, name='detail'),
    path('delete/<int:id>/', delete, name='delete'),
    path('create-comment/<int:post_id>/',create_comment,name="create-comment")   
]
