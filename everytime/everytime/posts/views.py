from django.shortcuts import render, redirect
from .models import Post,Comment
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    posts=Post.objects.all().order_by('-id')
    return render(request,'posts/main.html',{'posts':posts})

@login_required
def create(request):
    if request.method=="POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        is_anonymouse=request.POST.get('is_anonymouse')=='on'
        
        Post.objects.create(
            title=title,
            content=content,
            author=request.user,
            is_anonymouse=is_anonymouse
        )

        return redirect('posts:main')
    return redirect('posts:main')

def detail(request,id):
    post=get_object_or_404(Post,id=id)
    comments = post.comments.all().order_by('id')  
    return render(request,'posts/detail.html',{'post':post, 'comments':comments})

def update(request, id):
    post=get_object_or_404(Post,id=id)
    if request.method=="POST":
        post.title=request.POST.get('title')
        post.content=request.POST.get('content')
        post.is_anonymouse=request.POST.get('is_anonymouse')=='on'
        post.save()
        return redirect('posts:detail',id)
    return render(request,'posts/update.html',{'post':post})

def delete(request, id):
    post=get_object_or_404(Post,id=id)
    post.delete()
    return redirect('posts:main')

@login_required
def create_comment(request, post_id):
    post=get_object_or_404(Post,id=post_id)
    if request.method=="POST":
        content=request.POST.get('content')
        is_anonymouse=request.POST.get('is_anonymouse')=='on'

        Comment.objects.create(
            post=post, # 어떤 글에 댓글 달렸는지
            content=content,
            author=request.user, # 작성자
            is_anonymouse=is_anonymouse
        )

        return redirect('posts:detail',post_id)
    return redirect('posts:detail')

def delete_comment(request, comment_id):
    comment=get_object_or_404(Comment,id=comment_id)
    post_id=comment.post.id

    if request.user == comment.author:
        comment.delete()

    return redirect('posts:detail',post_id)
    
