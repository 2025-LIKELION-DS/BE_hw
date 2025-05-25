from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required


def main(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user.nickname  
        is_anonymous = 'is_anonymous' in request.POST

        Post.objects.create(
        title=title,
        content=content,
        author=author,  # 실제 닉네임 저장
        is_anonymous=is_anonymous  # 체크박스 여부
        )
        return redirect('posts:main')  # 작성 후 메인으로 리다이렉트

    posts = Post.objects.all().order_by('created_at')  # 오래된 순
    return render(request, 'posts/main.html', {'posts': posts})

def detail(request,id):
    post=get_object_or_404(Post,id=id)
    return render(request,'posts/detail.html',{'post':post})

def update(request,id):
    post=get_object_or_404(Post,id=id)
    
    if request.method=='POST':
        post.title=request.POST.get('title')
        post.content=request.POST.get('content')
        post.is_anonymous = 'is_anonymous' in request.POST
        post.save()
        return redirect('posts:detail', id)
    return render(request,'posts/update.html',{'post':post})

def delete(request,id):
    post=get_object_or_404(Post,id=id)
    post.delete()
    return redirect('posts:main')

@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        content = request.POST.get("content")
        is_anonymous = request.POST.get("is_anonymous") == "on"
        created_at=request.POST.get('created_at')

        Comment.objects.create(
            post=post,
            content=content,
            author="익명" if is_anonymous else request.user.nickname,  
            is_anonymous=is_anonymous,
            created_at=created_at
        )
        return redirect("posts:detail", id=post_id)
