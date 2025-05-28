from django.shortcuts import render
from .models import *
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def list(request):
    categories=Category.objects.all()
    category_id=request.GET.get('category')

    if category_id:
        """ 
        # 역참조
        category=get_object_or_404(Category,id=category_id)
        posts=category.posts.all().order_by('-id')
        """
        # filter 메소드 사용
        posts=Post.objects.filter(category__id=category_id).order_by('-id')
        # ManyToMayField : filter(다대다필드명__id=값)
        # ForeignKey : filter(외래키필드명=값)

    else:
        posts=Post.objects.all().order_by('-id')
    return render(request,'blog/list.html',{'posts':posts, 'categories':categories})

@login_required

def create(request):
    categories=Category.objects.all()

    if request.method == "POST":
        title=request.POST.get('title')
        content=request.POST.get('content')

        category_ids=request.POST.getlist('category')
        category_list=[get_object_or_404(Category, id=category_id) for category_id in category_ids]

        post=Post.objects.create(
            title=title,
            content=content,
            author=request.user
        )
        for category in category_list:
            post.category.add(category)

        return redirect('blog:list')
    return render(request,'blog/create.html',{'categories':categories})

def detail(request, id):
    post=get_object_or_404(Post,id=id)
    return render(request,'blog/detail.html',{'post':post})

def update(request, id):
    post=get_object_or_404(Post,id=id)

    if request.method=='POST':
        post.title=request.POST.get('title')
        post.content=request.POST.get('content')
        post.save()
        return redirect('blog:detail',id)
    return render(request,'blog/update.html',{'post':post})

def delete(request,id):
    post=get_object_or_404(Post,id=id)
    post.delete()
    return redirect('blog:list')

@login_required

def create_comment(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    if request.method == "POST":
        content=request.POST.get('content')

        Comment.objects.create(
            post=post,
            content=content,
            author=request.user
        )
        return redirect('blog:detail',post_id)
    return redirect('blog:list')

@login_required
def like(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    user=request.user

    # if user in post.like.all():  게시물의 좋아요 (Post의 like 필드) - 정참조
    if post in user.like_posts.all(): # 역참조 방식
        post.like.remove(user)
    else:
        post.like.add(user)
    return redirect('blog:detail',post_id)
