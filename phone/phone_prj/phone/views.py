from django.shortcuts import render
from .models import ContactInfo

def list(request):
    contacts = ContactInfo.objects.all().order_by('name')
    return render(request, 'phone/list.html',{'contacts':contacts})

def result(request):
    keyword = request.GET.get('keyword')
    contacts = ContactInfo.objects.filter(name__contains=keyword).order_by('name')
    return render(request, 'phone/result.html', {'contacts': contacts, 'keyword': keyword})