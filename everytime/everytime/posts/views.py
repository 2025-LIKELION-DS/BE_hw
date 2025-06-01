from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

def main(request):
    categories = Category.objects.all()
    category_posts = [(category, category.posts.all().order_by('-id')[:4]) for category in categories]
    return render(request, 'posts/main.html', {'categories':categories, 'category_posts':category_posts})

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    is_author = request.user.is_authenticated and post.author == request.user.nickname

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

    if post.author != request.user.nickname:
        return redirect('posts:detail', id=id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.is_anonymous = request.POST.get('is_anonymous') == 'on'
        post.save()
        return redirect('posts:detail', id=post.id)

    return render(request, 'posts/update.html', {'post': post})


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all().order_by('-id')

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_anonymous = request.POST.get('is_anonymous') == 'on'

        post = Post.objects.create(
            title = title,
            content = content,
            is_anonymous = is_anonymous,
            author=request.user
        )

        post.category.add(category)

        return redirect('posts:category', slug)
    return render(request, 'posts/category.html', {'posts':posts, 'category':category})

def like(request, post_id): 
    if request.method =="POST":
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        if user in post.like.all():
            post.like.remove(user)
        else:
            post.like.add(user)
        return redirect('posts:detail', post_id)

def scrap(request, post_id): 
    if request.method =="POST":
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        if user in post.scrap.all():
            post.scrap.remove(user)
        else:
            post.scrap.add(user)
        return redirect('posts:detail', post_id)
