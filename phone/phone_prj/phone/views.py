from django.shortcuts import render
from .models import Post
# Create your views here.

def list(request):
    posts = Post.objects.all().order_by('name')
    return render(request, 'phone/list.html', {'posts': posts})

def result(request):
    hint = request.GET.get('search')
    posts = Post.objects.filter(name__contains=hint)  # contains 필터 적용
    return render(request, 'phone/result.html', {'posts': posts, 'hint': hint})
