from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Phone
# Create your views here.
def list(request):
    phones = Phone.objects.all().order_by('name')
    return render(request, 'phone/list.html', {'phones':phones})

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num')
        email = request.POST.get('email')

        phone = Phone.objects.create(
            name = name,
            phone_num = phone_num,
            email = email
        )
        return redirect('phone:list')
    return render(request, 'phone/create.html')

def result(request):
    keyword = request.GET.get('keyword','')
    if keyword:
        phones = Phone.objects.filter(name__contains=keyword).order_by('name')
    else:
        phones = []
    
    context = {
        'keyword' : keyword,
        'phones' : phones,
    }
    return render(request, 'phone/result.html', context)