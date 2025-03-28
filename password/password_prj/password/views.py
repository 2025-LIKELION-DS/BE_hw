from django.shortcuts import render
import random
# Create your views here.
def index(request):
    return render(request, 'index.html')

def error1(request):
    return render(request, 'error1.html')

def error2(request):
    return render(request, 'error1.html')

def error3(request):
    return render(request, 'error1.html')


def password_generator(request):
    #form 정보 가져오기
    length = request.GET["length"]
    upper = "upper" in request.GET
    lower = "lower" in request.GET
    digits = "digits" in request.GET
    special = "special" in request.GET
        
    #문자 set 설정
    check_chars=''
    if upper:
        check_chars+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lower:
        check_chars+="abcdefghijklmnopqrstuvwxyz"
    if digits:
        check_chars+="0123456789"
    if special:
        check_chars+="!@#$%^&*"
    

    
    if length=='':
        return render(request,"error1.html")
    elif int(length)<=0:
        return render(request,"error2.html")
    elif not(upper or lower or digits or special):
        return render(request,"error3.html")
    else:
        random_password ="".join(random.choices(check_chars, k=int(length)))
        return render(request,"result.html",{"password":random_password})