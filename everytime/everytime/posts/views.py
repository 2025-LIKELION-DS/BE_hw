from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.

def main(request):
    posts=Post.objects.all().order_by('-id')
    return render(request, 'posts/main.html', {'posts':posts})

def create(request):
    if request.method=='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        is_anonymous = request.POST.get('is_anonymous')== 'on'

        Post.objects.create(
            title=title,
            content=content,
            author=request.user,
            is_anonymous=is_anonymous,
        )
        
        return redirect('posts:main')
    return render(request, 'posts/main.html')

def detail(request, id):
    post=get_object_or_404(Post, id=id)
    comments = post.comments.order_by('id')
    return render(request, 'posts/detail.html', {'post':post, 'comments':comments})

def update(request, id):
    post=get_object_or_404(Post, id=id)

    if request.method=="POST":
        post.tile=request.POST.get('title')
        post.content=request.POST.get("content")
        post.is_anonymous = request.POST.get('is_anonymous') =='on'
        post.save()
        return redirect('posts:detail', id)
    
    return render(request, 'posts/update.html', {'post':post})

def delete(request, id):
    post=get_object_or_404(Post, id=id)
    post.delete()
    return redirect('posts:main')

def create_comment(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    if request.method=='POST':
        content=request.POST.get('content')
        is_anonymous = request.POST.get('is_anonymous')== 'on'

        Comment.objects.create(
            post=post,
            content=content,
            author=request.user,
            is_anonymous=is_anonymous,
        )
        return redirect('posts:detail', post_id)
    return redirect('posts:main')

def delete_comment(request, comment_id):
    comment=get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('posts:detail', id=comment.post.id)
