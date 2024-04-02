from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def cart(request):
    return render(request,'cart.html')
def user_login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    else:
        user=request.POST['uname']
        psd=request.POST['upass']
        cpsd=request.POST['ucpass']
        print(user,psd,cpsd)
        u= User.objects.create(username=user,email=user,password=psd)
        u.set_password(psd)
        u.save()
        return HttpResponse('inserted')




