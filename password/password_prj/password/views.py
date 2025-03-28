from django.shortcuts import render
import random
# Create your views here.

def index(request):
    return render(request, 'index.html')

def error1(request):
    return render(request, 'error1.html')

def error2(request):
    return render(request, 'error2.html')

def error3(request):
    return render(request, 'error3.html')

def password_generator(request):
    length=request.GET['length']
    upper="upper" in request.GET
    lower="lower" in request.GET
    digits="digits" in request.GET
    special="special" in request.GET

    if length=='':
        return render(request, 'error2.html')
    
    length=int(length)
    
    if length<0:
        return render(request, 'error1.html')
    if upper==False and lower==False and digits==False and special==False :
        return render(request, 'error3.html')
    

    
    check_chars=""
    if upper:
        check_chars+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lower:
        check_chars+="abcdefghijklmnop"
    if digits:
        check_chars+="0123456789"
    if special:
        check_chars+="!@#$%^&*"

    result = ''.join(random.sample(check_chars, length))

    return render(request, 'result.html', {'upper':upper, 'lower':lower, 'digits':digits, 'special':special,
                                           'result':result})
