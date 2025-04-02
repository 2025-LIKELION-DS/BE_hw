from django.shortcuts import render
from .models import Phone

# Create your views here.

def list(request):
    phones = Phone.objects.all().order_by('name')
    return render(request, 'phone/list.html', {'phones':phones})

def result(request):
    keyword = request.GET['keyword']
    phones = Phone.objects.filter(name__contains=keyword).order_by('name')
    return render(request, 'phone/result.html', {'keyword':keyword, 'phones':phones})