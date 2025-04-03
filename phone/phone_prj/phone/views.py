from django.shortcuts import render, redirect
from .models import Phone

# Create your views here.

def list(request):
    phones=Phone.objects.all().order_by("name") #이름순으로 정렬하기
    return render(request, 'phone/list.html', {'phones':phones})

def result(request):
    searchWord = request.GET.get('searchWord')  
    phones = Phone.objects.filter(name__contains=searchWord).order_by("name")  
    #이름에 searchWord가 들어간 객체들의 쿼리셋을 빈환 후 이름 순으로 정렬 

    return render(request, 'phone/result.html', {'searchWord': searchWord, 'phones': phones})
