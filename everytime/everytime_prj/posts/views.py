from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required


def main(request):
    secret_category = Category.objects.get(slug='secret')
    freshman_category = Category.objects.get(slug='freshman')
    free_category = Category.objects.get(slug='free')

    secret_posts = Post.objects.filter(post_categories__category=secret_category).order_by('-created_at')[:4]
    freshman_posts = Post.objects.filter(post_categories__category=freshman_category).order_by('-created_at')[:4]
    free_posts = Post.objects.filter(post_categories__category=free_category).order_by('-created_at')[:4]

    return render(request, 'posts/main.html', {
        'secret_posts': secret_posts,
        'freshman_posts': freshman_posts,
        'free_posts': free_posts,
    })

@login_required
def detail(request,id):
    post=get_object_or_404(Post,id=id)
    return render(request,'posts/detail.html',{'post':post})

@login_required
def update(request,id):
    post=get_object_or_404(Post,id=id)
    
    if request.method=='POST':
        post.title=request.POST.get('title')
        post.content=request.POST.get('content')
        post.is_anonymous = request.POST.get("is_anonymous") == "on"
        post.save()
        return redirect('posts:detail', id)
    return render(request,'posts/update.html',{'post':post})

@login_required
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

@login_required
def category(request, slug):
    category = get_object_or_404(Category, slug=slug)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_anonymous = request.POST.get("is_anonymous") == "on"
  
        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user,
            is_anonymous=is_anonymous  
        )

        PostCategory.objects.create(post=post, category=category)

        return redirect('posts:category', slug=slug)

    posts = Post.objects.filter(category=category).order_by('-created_at')
    return render(request, 'posts/category.html', {'category': category, 'posts': posts})

@login_required
def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    
    if post in user.like_posts.all():
        user.like_posts.remove(post)
    else:
        user.like_posts.add(post)
    return redirect('posts:detail', post_id)

@login_required
def scrap(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    
    if post in user.scrapped_posts.all():
        user.scrapped_posts.remove(post)
    else:
        user.scrapped_posts.add(post)
    return redirect('posts:detail', post_id)