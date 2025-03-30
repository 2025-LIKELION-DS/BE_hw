from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request,'index.html')

def error1(request):
    return render(request,'error1.html')

def error2(request):
    return render(request,'error2.html')

def error3(request):
    return render(request,'error3.html')

def password_generator(request): # 비밀번호 생성성
    length = request.GET['length']
    upper="upper" in request.GET
    lower="lower" in request.GET
    digits="digits" in request.GET
    special="special" in request.GET

    if length=='': # 빈 문자열 입력
        return error2(request)
    
    if int(length)<=0: # 음수 입력
        return error1(request)

    # 체크 박스 선택에 따른 문자 집합 구성성
    check_chars=""

    if upper: # 대문자
        check_chars+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lower: # 소문자
        check_chars+="abcdefghijklmnopqrstuvwxyz"
    if digits: # 숫자
        check_chars+="0123456789"
    if special: #특수 문자  
        check_chars+="!@#$%^&*"

    if check_chars=="": # 옵션 선택 x
        return error3(request)

    password = ''.join(random.choices(check_chars, k=int(length))) # 비밀번호 생성

    return render(request,'result.html',{'password':password})    