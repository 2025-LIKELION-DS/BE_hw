from django.shortcuts import render, redirect, get_object_or_404
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

def create(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone_num=request.POST.get('phone_num')
        email=request.POST.get('email')

        phone=Phone.objects.create(
            name=name,
            phone_num=phone_num,
            email=email
        )
        return redirect('phone:list')
    return render(request, 'phone/create.html')

def detail(request, id):
    phone=get_object_or_404(Phone, id=id)
    return render(request, 'phone/detail.html', {'phone':phone})

def update(request, id):
    phone=get_object_or_404(Phone, id=id)

    if request.method=="POST":
        phone.name=request.POST.get('name')
        phone.phone_num=request.POST.get('phone_num')
        phone.email=request.POST.get('email')
        phone.save()
        return redirect('phone:list')
    return render(request, 'phone/update.html', {'phone': phone})

def delete(request, id):
    phone=get_object_or_404(Phone, id=id)
    
    if request.method=="POST":
        phone.delete()
        return redirect('phone:list')
    return render(request, 'phone/delete.html', {'phone':phone})
        
    