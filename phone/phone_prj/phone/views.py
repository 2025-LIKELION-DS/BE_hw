from django.shortcuts import render
from .models import Phone
from django.shortcuts import get_object_or_404

# Create your views here.
def list(request):
    phones=Phone.objects.all().order_by('name') # 이름순으로
    return render(request,'phone/list.html',{'phones':phones}) 
    # 'list.html' x -> templates>phone>list.html이므로 phone/list.html

def result(request):
    if request.method=='GET':
        keyword=request.GET.get('keyword') # 검색어 부분 받기
        result=Phone.objects.all() # 모든 전화번호 list 받기

        if keyword:
            result=result.filter(name__contains=keyword).order_by('name')
            # 이름 필터링 
             # //필드__contains : 대소문자 구분, 특정 문자열 포함되어 있는지 확인
            
    return render(request, 'phone/result.html',{'result':result,'keyword':keyword})