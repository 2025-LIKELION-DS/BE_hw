from django.shortcuts import render
from .models import Phone
from django.shortcuts import get_object_or_404

# Create your views here.
def list(request):
    phones=Phone.objects.all().order_by('name') # 이름순으로
    return render(request,'phone/list.html',{'phones':phones}) 
    # 'list.html' x -> templates>phone>list.html이므로 phone/list.html

def result(request):
    keyword=request.GET.get('keyword') # 검색어 부분 받기
    result = Phone.objects.filter(name__contains = keyword).order_by('name')
            
    return render(request, 'phone/result.html',{'result':result,'keyword':keyword})