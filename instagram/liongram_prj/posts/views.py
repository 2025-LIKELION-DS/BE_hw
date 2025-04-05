from django.shortcuts import render,redirect
from .models import Post
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.
def list(request):
    posts=Post.objects.all().order_by('-id') # 최신순 정렬
    return render(request,'posts/list.html',{'posts':posts})

def create(request):
    if request.method=="POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        
        post=Post.objects.create(
            title=title,
            content=content
        )
        return redirect('posts:list')
    return render(request,'posts/create.html')

def detail(request,id):
    posts=get_object_or_404(Post,id=id)
    posts.views+=1 # 조회수 +1
    posts.save() 
    return render(request,'posts/detail.html',{'posts':posts})

def update(request,id):
    posts=get_object_or_404(Post,id=id)

    if request.method=="POST":
        posts.title=request.POST.get('title')
        posts.content=request.POST.get('content')
        posts.save()
        return redirect('posts:detail',id)
    return render(request,'posts/update.html',{'posts':posts})

def delete(request,id):
    posts=get_object_or_404(Post,id=id)
    posts.delete()
    return redirect('posts:list')

def result(request):
    keyword=request.GET.get('keyword') # 검색어 받기
    posts=Post.objects.filter(Q(title__contains=keyword)|Q(content__contains=keyword)).order_by('-id')
    # 제목 키워드 or 내용 키워드 포함 시 검색
    return render(request,'posts/result.html',{'keyword':keyword,'posts':posts})
