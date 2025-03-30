from django.shortcuts import render
import random

def index(request):
    return render(request, 'password/index.html')

def error1(request):
    return render(request, 'password/error1.html')

def error2(request):
    return render(request, 'password/error2.html')

def error3(request):
    return render(request, 'password/error3.html')


def password_generator(request):
    if not request.GET.get('lenpwd'):
        return render (request,'password/error2.html')
    
    lenpwd=int(request.GET.get('lenpwd'))
    if (lenpwd<0): 
        return render(request,'password/error1.html')

    upper='upper' in request.GET
    lower='lower' in request.GET
    digits='digits' in request.GET
    special='special' in request.GET

    if not (upper or lower or digits or special):
        return render(request, 'password/error3.html')

    check_chars=''
    if upper:
        check_chars+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lower:
        check_chars+="abcdefghijklmnopqrstuvwxyz"
    if digits:
        check_chars+="0123456789"
    if special:
        check_chars+="!@#$%^&*"
    
    resultpwd=''
    for _ in range(lenpwd):
        resultpwd+=random.choice(check_chars)

    context={
        'resultpwd': resultpwd,
    }
    return render(request, 'password/result.html', context)