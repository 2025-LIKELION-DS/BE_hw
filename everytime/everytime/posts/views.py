from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

def main(request):
    return render(request, 'posts/main.html')