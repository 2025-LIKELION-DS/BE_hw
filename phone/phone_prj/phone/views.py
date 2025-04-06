from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView
from .models import Post
# Create your views here.

class ListView(ListView):
    queryset= Post.objects.all().order_by('name') #사용할 모델 
    template_name = 'phone/list.html' # 이 뷰에서 사용할 템플릿 파일의 경로 지정
    context_object_name = 'posts' #템플릿에서 사용할 객체의 이름 설정

def list(request):
    posts = Post.objects.all().order_by('name')
    return render(request, 'phone/list.html', {'posts': posts})

def result(request):
    hint = request.GET.get('search')
    posts = Post.objects.filter(name__contains=hint)  # contains 필터 적용
    return render(request, 'phone/result.html', {'posts': posts, 'hint': hint})

def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone_num = request.POST.get("number")
        email = request.POST.get("email")

        phone = Post.objects.create(
            name = name, 
            phone_num = phone_num, 
            email = email
        )

        return redirect('phone:list')
    return render(request, 'phone/create.html')

def detail(request,id):
    phone = get_object_or_404(Post,id=id)
    return render(request, 'phone/detail.html', {'phone':phone})

def delete(request,id):
    phone = get_object_or_404(Post,id=id)

    if request.method == "POST":
        phone.delete()
        return redirect('phone:list')
    return render(request,'phone/delete.html', {'phone':phone})

def update(request,id):
    phone = get_object_or_404(Post,id=id)

    if request.method == "POST":
        phone.name = request.POST.get("name") #뒤에 name은 create에서 내가 input에 설정한 이름. 앞에 phone.name에 name은 모델에서 설정한 이름.
        phone.phone_num = request.POST.get("number") # 앞에 phone은 phone = get_object_or_404(Post,id=id) 여기서 받아왔기 때문에
        phone.email = request.POST.get("email")
        phone.save()
    
        return redirect('phone:list')
    return render(request, 'phone/update.html', {'phone':phone})
