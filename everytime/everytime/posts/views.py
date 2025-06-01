from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def main(request):
    categories=Category.objects.all()

    secret_posts = Post.objects.filter(category__slug='secret').order_by('-id')[:4]
    freshman_posts = Post.objects.filter(category__slug='freshman').order_by('-id')[:4]
    free_posts = Post.objects.filter(category__slug='free').order_by('-id')[:4]
    # category.slug='secret' 이런식은 안됨 언더바 두개로 연결... join이란 뜻 (근데 코드 이런 식으로 쓰는 거 좀 비효율적인 거 같아요... 어떻게 하면 좋을까요...) 
    
    return render(request, 'posts/main.html', {'categories':categories, 'secret_posts': secret_posts,'freshman_posts': freshman_posts,'free_posts': free_posts})

@login_required
def create(request):
    categories=Category.objects.all()

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
    return render(request, 'posts/main.html', {'categories':categories})

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


@login_required
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

"""
def delete_comment(request, comment_id):
    comment=get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('posts:detail', id=comment.post.id)"""

@login_required
def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, post_id=post_id)
    comment.delete()
    
    return redirect('posts:detail', post_id=post_id)

@login_required
def category(request, slug):
    categories=get_object_or_404(Category, slug=slug)

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_anonymous = request.POST.get('is_anonymous') == 'on'

        post = Post.objects.create(
            title=title,
            content=content,
            is_anonymous=is_anonymous,
            author=request.user
        )
        post.category.add(categories)

        return redirect('posts:category', slug=slug)
    posts = categories.posts.all().order_by('-id')

    return render(request, 'posts/category.html', {'categories': categories, 'posts':posts})

@login_required
def like(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    user=request.user

    if post in user.like_posts.all(): 
        post.like.remove(user)
    else:
        post.like.add(user)
    return redirect('posts:detail', post_id)

@login_required
def scrap(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    user=request.user

    if post in user.scrap_posts.all(): 
        post.scrap.remove(user)
    else:
        post.scrap.add(user)
    return redirect('posts:detail', post_id)

    