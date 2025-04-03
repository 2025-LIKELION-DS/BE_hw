from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone

# Create your views here.

def list(request):
    phones = Phone.objects.all().order_by('name')
    return render(request, 'phone/list.html', {'phones':phones})

def result(request):
    keyword = request.GET['keyword']
    phones = Phone.objects.filter(name__contains=keyword).order_by('name')
    return render(request, 'phone/result.html', {'keyword':keyword, 'phones':phones})

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        phone = Phone.objects.create(
            name = name,
            number = number,
            email = email
        )
        return redirect('phone:list')
    return render(request, 'phone/create.html')

def detail(request, id):
    phone = get_object_or_404(Phone, id=id)
    return render(request, 'phone/detail.html', {'phone':phone})

def update(request, id):
    phone = get_object_or_404(Phone, id=id)
    if request.method == "POST":
        phone.name=request.POST.get('name')
        phone.number=request.POST.get('number')
        phone.email=request.POST.get('email')
        phone.save()
        return redirect('phone:detail', id)
    return render(request, 'phone/update.html', {'phone':phone})

def delete(request, id):
    phone = get_object_or_404(Phone, id=id)
    if request.method == "POST":
        phone.delete()
        return redirect('phone:list')
    return render(request, 'phone/delete.html', {'phone':phone})