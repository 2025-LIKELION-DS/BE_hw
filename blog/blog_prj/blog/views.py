from django.shortcuts import render
from .models import Post
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
# Create your views here.

def list(request):
    posts = Post.objects.all().order_by('-id') #id 역순으로 가져오겠다는 뜻. 디비 (최신글부터 볼 수 있음)
    
    return render(request, 'blog/list.html', {'posts':posts})

def create(request):
    if request.method =="POST":
        title = request.POST.get('title') 
        content = request.POST.get('content')

        post = Post.objects.create(
            title=title,
            content= content
        )

        return redirect('blog:list') #데이터 전송없이 url 이동만
    return render(request, 'blog/create.html') 

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render (request, 'blog/detail.html', {'post':post})

def update(request,id):
    post = get_object_or_404(Post, id=id)

    if request.method =='POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()

        return redirect ('blog:detail', id)
    return render(request, 'blog/update.html', {'post':post})
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect ('blog:list')



