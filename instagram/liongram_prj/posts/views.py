from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Post

# 메인 페이지
def list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'posts/list.html', {'posts':posts})

# 키워드 검색 결과
def result(request):
    keyword = request.GET.get('keyword')
    # 사용자가 입력한 키워드를 포함하고 있는 title 필드 및 content 필드
    posts = Post.objects.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword))
    return render(request, 'posts/result.html', {'keyword': keyword, 'posts':posts})

# 글 작성하기
def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        post = Post.objects.create(
            title = title,
            content = content
        )
        return redirect('posts:list')
    return render(request, 'posts/create.html')

# 글 상세 페이지
def detail(request, id):
    post = get_object_or_404(Post, id=id)
    post.views += 1               # detail 페이지에 들어갈 때마다 해당 데이터의 조회수가 +1 되도록
    post.save()
    return render(request, 'posts/detail.html', {'post':post})

#글 수정하기
def update(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('posts:detail', id)
    return render(request, 'posts/update.html', {'post': post})

#글 삭제하기
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('posts:list')
