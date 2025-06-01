from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    categories=Category.objects.all()
    category_posts=[]

    for category in categories:
        posts = category.category_posts.all().order_by('-created_at')[:4]
        category_posts.append((category, posts))

    return render(request,'posts/main.html',{'categories':categories,'category_posts':category_posts})

@login_required
def create(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_anonymouse = 'is_anonymouse' in request.POST

        category_ids=request.POST.getlist('category')
        category_list=[get_object_or_404(Category,id=category_id)for category_id in category_ids]
        
        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user,
            is_anonymouse=is_anonymouse
        )

        for category in category_list:
            post.category.add(category)

        return redirect('posts:main')
    return render(request, 'posts/create.html',{'categories':categories})

def detail(request,id):
    post=get_object_or_404(Post,id=id)
    comments = post.comments.all().order_by('id')  
    return render(request,'posts/detail.html',{'post':post, 'comments':comments})

def update(request, id):
    post=get_object_or_404(Post,id=id)
    if request.method=="POST":
        post.title=request.POST.get('title')
        post.content=request.POST.get('content')
        post.is_anonymouse = 'is_anonymouse' in request.POST
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
        is_anonymouse = 'is_anonymouse' in request.POST

        Comment.objects.create(
            post=post, # 어떤 글에 댓글 달렸는지
            content=content,
            author=request.user, # 작성자
            is_anonymouse=is_anonymouse
        )

        return redirect('posts:detail',post_id)

@login_required
def delete_comment(request, comment_id):
    comment=get_object_or_404(Comment,id=comment_id)
    post_id=comment.post.id

    if request.user == comment.author:
        comment.delete()

    return redirect('posts:detail',post_id)
    
def category(request,slug):
    category=get_object_or_404(Category,slug=slug)
    posts=category.category_posts.all().order_by('-created_at')
    return render(request,'posts/category.html',{'posts':posts,'category':category})

def like(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    user=request.user

    if user in post.like.all():
        post.like.remove(user)
    else:
        post.like.add(user)
    return redirect('posts:detail',post_id)

def scrap(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    user=request.user

    if user in post.scrap.all():
        post.scrap.remove(user)
    else:
        post.scrap.add(user)
    return redirect('posts:detail',post_id)