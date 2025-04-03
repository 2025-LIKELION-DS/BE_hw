from django.shortcuts import render, redirect
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
    return render(request,'phone/create.html')

def detail(request,id):
    phone=get_object_or_404(Phone,id=id)
    return render(request,'phone/detail.html',{'phone':phone})

def update(request,id):
    phone=get_object_or_404(Phone,id=id)
    if request.method=="POST":
        phone.name=request.POST.get('name')
        phone.phone_num=request.POST.get('phone_num')
        phone.email=request.POST.get('email')
        phone.save()
        redirect('phone:detail',id)
    return render(request,'phone/update.html', {'phone': phone})

def delete(request,id):
    phone=get_object_or_404(Phone,id=id)

    if request.method == "POST":  
        phone.delete()
        return redirect('phone:list')

    return render(request, 'phone/delete.html', {'phone': phone})