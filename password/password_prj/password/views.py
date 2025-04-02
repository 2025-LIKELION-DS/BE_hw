from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request,'index.html')

def password_generator(request): # 비밀번호 생성성
    length = request.GET['length']
    upper="upper" in request.GET
    lower="lower" in request.GET
    digits="digits" in request.GET
    special="special" in request.GET

    if length=='': # 빈 문자열 입력
        return render(request, "error2.html")
    
    if int(length)<=0: # 음수 입력
        return render(request, "error1.html")
    
    # 체크 박스 선택에 따른 문자 집합 구성
    check_chars=""

    if upper: # 대문자
        check_chars+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lower: # 소문자
        check_chars+="abcdefghijklmnopqrstuvwxyz"
    if digits: # 숫자
        check_chars+="0123456789"
    if special: #특수 문자  
        check_chars+="!@#$%^&*"

    if not (upper or lower or digits or special):
        return render(request, "error3.html")

    password = ''.join(random.choices(check_chars, k=int(length))) # 비밀번호 생성

    return render(request,'result.html',{'password':password})    