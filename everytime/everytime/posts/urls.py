from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', main, name='main'),
    path('detail/<int:id>/', detail, name='detail'),
    path('delete/<int:id>/', delete_post, name='delete'),
    path('comment/delete/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('update/<int:id>/', update_post, name='update'),
]