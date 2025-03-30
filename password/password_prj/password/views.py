from django.shortcuts import render
import random

# Create your views here.


def index(request):
    return render(request,'index.html')

#체크박스 선택에 따른 문자 집합 구성
def password_generator(request):
    length = request.GET.get('length') 

    if not length:
        return render(request,'error2.html')
    
    length = int(length)

    if length < 0 :
        return render(request, 'error1.html')

    
    upper = "upper" in request.GET
    lower = "lower" in request.GET
    digits = "digits" in request.GET
    special = "special" in request.GET

    check_chars = ""
    if upper:
        check_chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lower:
        check_chars += "abcdefghijklmnopqrstuvwxyz"
    if digits:
        check_chars += "0123456789"
    if special:
        check_chars += "!@#$%^&*"

    
    if not check_chars:
        return render(request,'error3.html')

    password = "".join(random.choice(check_chars) for _ in range(length))

    return render(request, 'result.html', {'password': password})
