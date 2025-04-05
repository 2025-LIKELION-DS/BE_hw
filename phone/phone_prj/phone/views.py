from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import ContactInfo

class IndexView(ListView):
    queryset = ContactInfo.objects.all().order_by('name')
    template_name = 'phone/list.html'
    context_object_name = 'contacts'

def result(request):
    keyword = request.GET.get('keyword')
    contacts = ContactInfo.objects.filter(name__contains=keyword).order_by('name')
    return render(request, 'phone/result.html', {'contacts': contacts, 'keyword': keyword})

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num')
        email = request.POST.get('email')

        phone = ContactInfo.objects.create(
            name = name,
            phone_num = phone_num,
            email = email
        )
        return redirect('phone:list')
    return render(request, 'phone/create.html')

def detail(request, id):
    contact = get_object_or_404(ContactInfo, id=id)
    return render(request, 'phone/detail.html', {'contact': contact})

def update(request, id):
    contact = get_object_or_404(ContactInfo, id=id)
    if request.method == "POST":
        contact.name = request.POST.get('name')
        contact.phone_num = request.POST.get('phone_num')
        contact.email = request.POST.get('email')
        contact.save()
        return redirect('phone:list')
    return render(request,'phone/update.html', {'contact': contact})   

def delete(request, id):
    contact = get_object_or_404(ContactInfo, id=id)
    if request.method == "POST":
        contact.name = request.POST.get('name')
        contact.delete()
        return redirect('phone:list')
    return render(request,'phone/delete.html', {'contact': contact})  


