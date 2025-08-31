from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

def main(request):
    categories = Category.objects.all().order_by('-id')
    for category in categories:
        category.latest_posts = category.posts.all().order_by('-id')[:4]
    return render(request, 'posts/main.html', {'categories': categories})

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
    categories = Category.objects.all()
    if request.method == "POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        is_anonymouse = request.POST.get('is_anonymouse') == 'true'
        category_id = request.POST.get('category_id')
        category = get_object_or_404(Category, id=category_id)
        image=request.FILES.get('image')
        video=request.FILES.get('video')

        post=Post.objects.create(
            title=title,
            content=content,
            author=request.user,
            is_anonymouse=is_anonymouse,
            image=image,
            video=video
        )
        post.category.add(category)
        return redirect('posts:category_list', slug=category.slug)
    return render(request,'posts/create.html', {'categories': categories})

def detail(request,id):
    post=get_object_or_404(Post,id=id)
    return render(request, 'posts/detail.html',{'post':post})

def update(request,id):
    post=get_object_or_404(Post,id=id)
    if request.method == 'POST':
        post.title=request.POST.get('title')
        post.content=request.POST.get('content')
        post.is_anonymouse = request.POST.get('is_anonymouse')== 'true'
        image = request.FILES.get('image')
        video = request.FILES.get('video')
        
        if image: 
            if post.image:  
                post.image.delete()
            post.image = image
        
        if video:  
            if post.video:
                post.video.delete()
            post.video = video

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

def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all().order_by('-id')
    return render(request, 'posts/category.html', {'category': category,'posts': posts})

@login_required
def like(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    user=request.user
    if post in user.posts_like.all(): 
        user.posts_like.remove(post)
    else:
        user.posts_like.add(post)
    return redirect('posts:detail', post_id)

@login_required
def scrap(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    user=request.user
    if post in user.posts_scrap.all(): 
        user.posts_scrap.remove(post)
    else:
        user.posts_scrap.add(post)
    return redirect('posts:detail', post_id)