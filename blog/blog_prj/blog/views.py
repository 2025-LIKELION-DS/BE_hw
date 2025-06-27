from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

def list(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')

    if category_id:
        category = get_object_or_404(Category, id = category_id)
        posts = Post.objects.filter(category=category).order_by('-id') 
        #왼쪽 `category`: → `Post` 모델 안의 ForeignKey 필드 이름
        #오른쪽 `category`: → `Category` 모델의 인스턴스(객체) 하나
    else:
        posts = Post.objects.all().order_by('-id') #id 역순으로 가져오겠다는 뜻. 디비 (최신글부터 볼 수 있음)
    
    return render(request, 'blog/list.html', {'posts':posts, 'categories' : categories})

@login_required
def create(request):
    categories = Category.objects.all()

    if request.method =="POST":
        title = request.POST.get('title') 
        content = request.POST.get('content')
        image = request.FILES.get('image')
        video = request.FILES.get('video')

        category_ids = request.POST.getlist('category')
        category_list = [get_object_or_404(Category, id=category_id) for category_id in category_ids]


        post = Post.objects.create(
            title=title,
            content= content,
            author=request.user,
            image = image,
            video = video
        )

        for category in category_list:
            post.category.add(category)

        return redirect('blog:list') #데이터 전송없이 url 이동만
    return render(request, 'blog/create.html', {'categories': categories}) 

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render (request, 'blog/detail.html', {'post':post})

def update(request,id):
    post = get_object_or_404(Post, id=id)

    if request.method =='POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        image = request.FILES.get('image')
        video = request.FILES.get('video')

        if image:
            post.image.delete()
            post.image = image
        
        if video:
            post.video.delete()
            post.video = video

        post.save()

        return redirect ('blog:detail', id)
    return render(request, 'blog/update.html', {'post':post})

def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect ('blog:list')

@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')

        Comment.objects.create(
            post=post,
            content=content,
            author=request.user
        )
        return redirect('blog:detail', post_id)
    return redirect('blog:list')

def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user= request.user

    if post in user.like_posts.all(): #사용자가 좋아요를 눌렀는지 확인하는 함수
        post.like.remove(user) #눌렀으면 취소한다 ( 두번 누르면 취소 )
    else:
        post.like.add(user)
    return redirect('blog:detail', post_id)


