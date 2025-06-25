from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

def main(request):
    categories = Category.objects.all()
    category_posts = [(category, category.posts.all().order_by('-id')[:4]) for category in categories]
    return render(request, 'posts/main.html', {'categories':categories, 'category_posts':category_posts})
    # posts = Post.objects.all().order_by('-created_at')
    # return render(request, 'posts/main.html', {'posts': posts})

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all().order_by('created_at')
    return render(request, 'posts/detail.html', {'post': post, "comments":comments})

@login_required
def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all().order_by('-id')

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_anonymous = 'is_anonymous' in request.POST

        post = Post.objects.create(
            title = title,
            content = content,
            is_anonymous = is_anonymous,
            author = request.user,
        )

        post.category.add(category)

        return redirect('posts:category', slug)
    return render(request, 'posts/category.html', {'category': category, 'posts': posts})

@login_required
def update_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.is_anonymous = 'is_anonymous' in request.POST
        post.save()
        return redirect('posts:detail', id=post.id)

    return render(request, 'posts/update.html', {'post': post})

@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    
    if post.author == request.user.username:
        post.delete()
        return redirect('posts:main')
    
    return redirect('posts:detail', id=id)

@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    anonymity = 'anonymity' in request.POST
    
    if request.method == "POST":
        Comment.objects.create(
            content = request.POST.get('content'),
            anonymity = anonymity,
            author = request.user,
            post = post
        )
    return redirect('posts:detail', post_id)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('posts:detail', id=comment.post.id)


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
