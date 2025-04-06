from django.shortcuts import render ,redirect, get_object_or_404
from django.db.models import Q
from .models import Post
# Create your views here.

def list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'posts/list.html', {'posts':posts})

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content =  request.POST.get('content')
    
        posts = Post.objects.create(
            title = title,
            content = content
        )
        
        return redirect('posts:list')
    return render(request,'posts/create.html')

def detail(request,id):
    posts = get_object_or_404(Post, id=id)
    posts.increase_views()
    return render(request, 'posts/detail.html', {'posts':posts})

def update(request, id):
    posts = get_object_or_404(Post, id=id)

    if request.method == "POST":
        posts.title = request.POST.get('title')
        posts.content =  request.POST.get('content')
        posts.save()

        return redirect('posts:detail',id=id)
    return render (request, 'posts/update.html', {'posts':posts})

def result(request):
    hint = request.GET.get('search')
    posts = Post.objects.filter(
        Q(title__contains=hint) | Q(content__contains=hint) 
        )
    return render(request, 'posts/result.html' , {'hint':hint , 'posts':posts})

def delete(request,id):
    posts=get_object_or_404(Post, id=id)
    posts.delete()
    return redirect ('posts:list')