from django.shortcuts import render
import random
# Create your views here.

def index(request):
    return render(request, 'index.html')

def password_generator(request):
    word_length = request.GET['wordlen']

    if not word_length:
        return render(request, 'error2.html')

    if int(word_length) <= 0:
        return render(request, 'error1.html')
    
    upper = "upper" in request.GET
    lower = "lower" in request.GET
    digits = "digits" in request.GET
    special = "special" in request.GET

    if not (upper or lower or digits or special):
        return render(request, 'error3.html')
    
    check_chars = ""
    if upper:
        check_chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lower:
        check_chars += "abcdefghijklmnopqrstuvwxyz"
    if digits:
        check_chars += "0123456789"
    if special:
        check_chars += "!@#$%^&*"

    password = ""
    for _ in range(int(word_length)):
        password += random.choice(check_chars)

    return render(request, 'result.html', {'password': password})