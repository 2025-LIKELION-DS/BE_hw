from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.db.models import Q

# Create your views here.


def list(request):
    posts=Post.objects.all().order_by('-id')
    return render(request, 'posts/list.html', {'posts':posts})

def create(request):
    if request.method=="POST":
        title=request.POST.get('title')
        content=request.POST.get('content')

        post=Post.objects.create(
            title=title,
            content=content
        )
        return redirect('posts:list')
    return render(request, 'posts/create.html')

def detail(request, id):
    post=get_object_or_404(Post, id=id)
    post.add_view()
    return render(request, 'posts/detail.html', {'post':post})

def update(request, id):
    post=get_object_or_404(Post, id=id)

    if request.method=="POST":
        post.title=request.POST.get('title')
        post.content=request.POST.get('content')
        post.save()
        return redirect('posts:detail', id)
    return render(request, 'posts/update.html', {'post':post})

def delete(request, id):
    post=get_object_or_404(Post, id=id)
    post.delete()
    return redirect('posts:list')

def result(request):
    searchWord=request.GET['searchWord']
    posts=Post.objects.filter(Q(title__contains=searchWord)|Q(content__contains=searchWord)).order_by('-id')
    return render(request, 'posts/result.html', {'searchWord':searchWord, 'posts':posts})