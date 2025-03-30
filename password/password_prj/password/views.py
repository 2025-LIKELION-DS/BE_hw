from django.shortcuts import render
import random

def index(request):
    return render(request,'password/index.html')

def password_generator(request):
    upper = "upper" in request.GET      #영어 대문자
    lower = "lower" in request.GET      #영어 소문자
    digits = "digits" in request.GET    #숫자
    special = "special" in request.GET  #특수기호

    try:
        length = int(request.GET.get('length'))            #비밀번호 길이 입력 여부
    except ValueError:
        return render(request, 'password/error2.html')

    if length < 0:                                         #비밀번호 음수값 여부
        return render(request, 'password/error1.html')
    if not (upper or lower or digits or special):          #체크박스 선택 여부
        return render(request, 'password/error3.html')

    password_chars = ""
    if upper:
        password_chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lower:
        password_chars += "abcdefghijklmnopqrstuvwxyz"
    if digits:
        password_chars += "0123456789"
    if special:
        password_chars += "!@#$%^&*"

    password = ''.join(random.choices(password_chars, k=length))

    return render(request,'password/result.html',{'password_result':password})