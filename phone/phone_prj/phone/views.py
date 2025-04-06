from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.views.generic import ListView

class ListView(ListView):
    queryset=Post.objects.all().order_by('name')
    template_name='phone/list.html'
    context_object_name='phones'

def list(request):
    phones = Post.objects.all().order_by('name')
    return render(request, 'phone/list.html', {'phones' : phones})

def result(request):
    search_name = request.GET.get('search_name')

    phones = Post.objects.filter(name__contains=search_name).order_by('name')

    context = {
        'phones' : phones,
        'search_name' : search_name
    }

    return render(request, 'phone/result.html', context)


def create(request):
    
    if request.method=="POST":
        name=request.POST.get("name")
        phone_num=request.POST.get("phone_num")
        email=request.POST.get("email")
        
        phone=Post.objects.create(
            name=name,
            phone_num=phone_num,
            email=email
        )    
        
        return redirect('phone:list')
        
    return render(request,'phone/create.html')

def detail(request,id):
    phone=get_object_or_404(Post,id=id)    
    return render(request,'phone/detail.html',{"phone":phone})

def update(request,id):
    
    phone=get_object_or_404(Post,id=id)
    
    if request.method=="POST":
        phone.name=request.POST.get("name")
        phone.phone_num=request.POST.get("phone_num")
        phone.email=request.POST.get("email")
        phone.save()
        return redirect('phone:detail', id)
    
    return render(request,'phone/update.html',{"phone":phone})

def delete(request,id):
    phone=get_object_or_404(Post,id=id)
    if request.method=="POST":
        phone.delete()
        return redirect('phone:list')
    return render(request,'phone/delete.html', {"phone":phone})

