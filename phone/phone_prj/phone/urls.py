from django.urls import path
from .views import IndexView, result, create, detail, update, delete

app_name='phone' 

urlpatterns=[
	path('', IndexView.as_view(), name='list'), 
    # CBV 형식 
    # / 이미 짜여진 코드의 name이 list였기에 name='list'로 고정
    path('result/',result,name='result'),
    path('create/',create,name='create'),
    path('detail/<int:id>',detail,name='detail'),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),
]