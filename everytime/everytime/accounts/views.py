from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from posts.models import Post

# 회원가입
def signup(request):
    if request.method=="GET":
        form=SignUpForm()
        return render(request,'accounts/signup.html',{'form':form})
    
    form=SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('accounts:login')
    else:
        return render(request,'accounts/signup.html',{'form':form})
    
# 로그인
def login(request):
    if request.method=="GET":
        return render(request,'accounts/login.html',{'form':AuthenticationForm})
    
    form=AuthenticationForm(request,request.POST)
    if form.is_valid():
        auth_login(request,form.user_cache)
        return redirect('posts:main')
    return render(request,'accounts/login.html',{'form':form})

# 로그아웃
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('posts:main')

# 마이페이지
def mypage(request):
    return render(request,'accounts/mypage.html')

# 유저 정보
def user_info(request):
    return render(request,'accounts/user_info.html')

# 내가 작성한 글
def mypost(request):
    myposts=request.user.posts.all().order_by('-created_at')
    return render(request,'accounts/mypost.html',{'myposts':myposts})

# 내가 스크랩한 글
def myscrap(request):
    scraped_posts=request.user.scraped_posts.all().order_by('-id') 
    return render(request,'accounts/myscrap.html',{'scraped_posts':scraped_posts})