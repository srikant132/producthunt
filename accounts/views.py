from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        #Usert has info and wants an accounts now!
        if request.POST['password1'] == request.POST['password2']:
           try:
               user = User.objects.get(username=request.POST['username'])
               return render(request,'accounts/signup.html',{'error':'Username is all ready taken'})
           except User.DoesNotExist:
                user= User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
             return render(request,'accounts/signup.html',{'error':'Passwords must match'})
    else:
        #user want to enter info
        return render(request,'accounts/signup.html')


def login(request):
    return render(request,'accounts/login.html')


def logout(request):
    # TODO  need to route to homepage
    # and dont forget to logout
    return render(request,'accounts/signup.html')
