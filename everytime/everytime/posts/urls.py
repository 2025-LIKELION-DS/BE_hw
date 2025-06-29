from django.urls import path
from .views import *

app_name='posts'

urlpatterns=[
    path('', main, name='main'),
    path('update/<int:id>', update, name='update'),
    path('detail/<int:id>', detail, name='detail'),
    path('delete/<int:id>', delete, name='delete'),
    path('create/', create_post, name='create'),
    path('create-comment/<int:post_id>', create_comment, name='create-comment'),
    #path('delete-comment/<int:comment_id>', delete_comment, name='delete-comment'), 수정 전 코드
    path('delete-comment/<int:post_id>/<int:comment_id>', delete_comment, name='delete-comment'),
    path('category/<slug:slug>', category, name='category'),
    path('add-like/<int:post_id>/', add_like, name='add-like'),
    path('remove-like/<int:post_id>/', remove_like, name='remove-like'),
    path('scrap/<int:post_id>/', scrap, name='scrap'),
]