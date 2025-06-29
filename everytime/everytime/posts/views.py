from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def main(request):
    categories = Category.objects.all()
    category_posts = []
    # 카테고리별 최신 글 4개 저장 (리스트 형태)
    for category in categories:
        posts = Post.objects.filter(category=category).order_by('-id')[:4]
        
        # 딕셔너리로 (카테고리, 게시글 4개) 한 쌍을 만들어 리스트에 추가
        category_posts.append({"category": category, "posts": posts})

    return render(request, 'posts/main.html', {'categories': categories, 'category_posts': category_posts})
    

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category).order_by('-id')

    return render(request, 'posts/category.html', {'posts': posts, 'category': category})

@login_required
def create_post(request, slug):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = Category.objects.get(slug=slug)
        is_anonymous = 'is_anonymous' in request.POST
        image=request.FILES.get('image')
        video=request.FILES.get('video')

        post = Post.objects.create(
            title = title,
            content = content,
            is_anonymous = is_anonymous,
            author = request.user,
            image=image,
            video=video,
        )
        post.category.add(category)

        return redirect('posts:category', slug)
    return render(request, 'posts/main.html', {'category': category})

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
        image=request.FILES.get('image')
        video=request.FILES.get('video')

        if image:
            post.image.delete()
            post.image=image

        if video:
            post.video.delete()
            post.video=video

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
        image=request.FILES.get('image')
        video=request.FILES.get('video')

        post = Post.objects.create(
            title=title,
            content=content,
            is_anonymous=is_anonymous,
            author=request.user,
            image=image,
            video=video,
        )
        post.category.add(categories)

        return redirect('posts:category', slug=slug)
    posts = categories.posts.all().order_by('-id')

    return render(request, 'posts/category.html', {'categories': categories, 'posts':posts})

@login_required
def add_like(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    user=request.user

    if post not in user.like_posts.all():
        post.like.add(user)
    return redirect('posts:detail', post_id)

def remove_like(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    user=request.user

    if post in user.like_posts.all():
        post.like.remove(user)
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

    