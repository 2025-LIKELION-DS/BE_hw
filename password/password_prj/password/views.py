from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'password/index.html')


def password_generator(request):
    #form에 입력된 정보 가져오기
    length = request.GET.get('length')
    #비밀번호 길이 입력 여부 확인
    if length is None:
        return render(request, 'password/error1.html')
    elif length.strip() == "":
        return render(request, 'password/error1.html')
    #비밀번호 음수값인지 확인
    if length.isdigit() == False:
        return render(request, 'password/error1.html')

    length = int(length)
    if length <= 0:
        return render(request, 'password/error2.html')
    
    #체크박스 선택했는지 확인
    upper = "upper" in request.GET
    lower = "lower" in request.GET
    digits = "digits" in request.GET
    special = "special" in request.GET
    #"요청에 체크박스 내용이 포함되어있는가?"
    if upper == False and lower == False and digits == False and special == False:
        return render(request, 'password/error3.html')
    
    #체크박스 선택에 따른 문자 집합(set) 구성
    check_chars = ""
    if upper:
        check_chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lower:
        check_chars += "abcdefghijklmnopqrstuvwxyz"
    if digits:
        check_chars += "0123456789"
    if special:
        check_chars += "!@#$%^&*"

    #비밀번호 생성
    password = ""
    i = 0
    while i < length:
        password += random.choice(check_chars)
        i += 1

    return render(request, 'password/result.html', {'password' : password})