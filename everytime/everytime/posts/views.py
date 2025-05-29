from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

def main(request):
    posts=Post.objects.all().order_by('-id')
    return render(request, 'posts/main.html',{'posts':posts,})

@login_required
def create_comment(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    if request.method=='POST':
        content=request.POST.get("content")
        is_anonymouse = request.POST.get('is_anonymouse') == 'true'

        Comment.objects.create(
            post=post,
            content=content,
            author=request.user,
            is_anonymouse=is_anonymouse
        )
        return redirect('posts:detail',post_id)
    return redirect('posts:detail')

@login_required
def create(request):
    if request.method == "POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        is_anonymouse = request.POST.get('is_anonymouse') == 'true'

        post=Post.objects.create(
            title=title,
            content=content,
            author=request.user,
            is_anonymouse=is_anonymouse
        )
        return redirect('posts:main')
    return render(request,'posts/create.html')

def detail(request,id):
    post=get_object_or_404(Post,id=id)
    return render(request, 'posts/detail.html',{'post':post})

def update(request,id):
    post=get_object_or_404(Post,id=id)
    if request.method == 'POST':
        post.title=request.POST.get('title')
        post.content=request.POST.get('content')
        post.is_anonymouse = request.POST.get('is_anonymouse')== 'true'
        post.save()
        return redirect('posts:detail',id)
    return render(request,'posts/update.html',{'post':post})

def delete(request, id):
    post= get_object_or_404(Post, id=id)
    post.delete()
    return redirect('posts:main')

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id 
    comment.delete()
    return redirect('posts:detail', post_id)