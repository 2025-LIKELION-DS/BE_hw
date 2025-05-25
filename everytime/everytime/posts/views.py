from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

def main(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        anonymous_value = request.POST.get('is_anonymous')
        author_name = request.user.nickname

        if anonymous_value == 'on':
            is_anonymous = True
        else:
            is_anonymous = False

        Post.objects.create(
            title=title,
            content=content,
            is_anonymous=is_anonymous,
            author=author_name
        )
        return redirect('posts:main')

    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/main.html', {'posts': posts})


def detail(request, id):
    post = get_object_or_404(Post, id=id)

    is_author = False
    if request.user.is_authenticated and post.author == request.user.nickname:
        is_author = True

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('accounts:login')

        content = request.POST.get('content')
        is_anonymous = request.POST.get('is_anonymous') == 'on'
        author_name = request.user.nickname

        Comment.objects.create(
            post=post,
            content=content,
            is_anonymous=is_anonymous,
            author=author_name
        )
        return redirect('posts:detail', id=post.id)

    comments = post.comments.all().order_by('created_at')
    return render(request, 'posts/detail.html', {'post': post, 'comments': comments, 'is_author': is_author})


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if post.author == request.user.nickname:
        post.delete()
        return redirect('posts:main')
    return redirect('posts:detail', id=id)


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author == request.user.nickname:
        comment.delete()
    return redirect('posts:detail', id=comment.post.id)


@login_required
def update_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.is_anonymous = request.POST.get('is_anonymous') == 'on'

        post.save()
        return redirect('posts:detail', id=post.id)

    return render(request, 'posts/update.html', {'post': post})