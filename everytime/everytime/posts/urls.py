from django.urls import path
from .views import *

app_name='posts'
urlpatterns = [
    path('',main,name='main'),
    path('create/',create, name='create'),
    path('detail/<int:id>/', detail,name='detail'),
    path('update/<int:id>/', update,name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('delete-comment/<int:comment_id>/', delete_comment, name='delete-comment'),
    path('create-comment/<int:post_id>/', create_comment, name='create-comment'),
    path('category/<slug:slug>/', category_list, name='category_list'),
    path('like/<int:post_id>/',like,name='like'),
    path('scrap/<int:post_id>/',scrap,name='scrap'),
]
