from django.shortcuts import render,redirect,get_object_or_404
from .models import Post

def list(request):
    phones = Post.objects.all().order_by('name')
    return render(request, 'phone/list.html', {'phones' : phones})

def result(request):
    search_name = request.GET.get('search_name')

    phones = Post.objects.filter(name__contains=search_name).order_by('name')

    context = {
        'phones' : phones,
        'search_name' : search_name
    }

    return render(request, 'phone/result.html', context)


