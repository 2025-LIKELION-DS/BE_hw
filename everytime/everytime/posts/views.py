from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import * 
# Create your views here.

def main(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_anonymous = request.POST.get('is_anonymous') == "on"  #체크박스 처리
        
        Post.objects.create(
            title=title, 
            content=content,
            author = request.user,
            is_anonymous = is_anonymous,
        )
        return redirect ('posts:main')
    else: # GET 요청일 때는 기존 글 목록 보여주기
        posts = Post.objects.all().order_by('-created_at')  # 최신 글부터
    return render(request, 'posts/main.html' , {'posts':posts})

def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render (request, 'posts/detail.html', {'post':post})


def update(request,id):
    post = get_object_or_404(Post, id=id)

    if request.method =='POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.is_anonymous = request.POST.get('is_anonymous') == "on"
        post.save()

        return redirect ('posts:detail', id)
    return render(request, 'posts/update.html', {'post':post})

def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect ('posts:main')

def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        is_anonymous = request.POST.get('is_anonymous') == "on"

        Comment.objects.create(
            post = post,
            content=content,
            author=request.user,
            is_anonymous = is_anonymous
        )
        return redirect('posts:detail', post_id)
    return redirect('posts:main')

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect ('posts:detail', post_id=comment.post.id)
