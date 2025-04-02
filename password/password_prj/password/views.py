from django.shortcuts import render
import random
# Create your views here.

def index(request):
    return render(request, 'password/index.html')


def password_generator(request):
    length=request.GET['length']
    upper="upper" in request.GET
    lower="lower" in request.GET
    digits="digits" in request.GET
    special="special" in request.GET

    if length=='':
        return render(request, 'password/error2.html')
    
    length=int(length)
    
    if length<0:
        return render(request, 'password/error1.html')
    if not (upper or lower or digits or special):
        return render(request, "password/error3.html")
    # 드모르간 법칙으로 수정
    

    
    check_chars=""
    if upper:
        check_chars+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lower:
        check_chars+="abcdefghijklmnopqrstuvwxyz"
    if digits:
        check_chars+="0123456789"
    if special:
        check_chars+="!@#$%^&*"

    result = ''.join(random.choices(check_chars, length))
    #sample -> choices로 수정

    return render(request, 'password/result.html', {'result':result})
