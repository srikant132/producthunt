from django.shortcuts import render

# Create your views here.
def signup(request):
    render(request,'accounts/signup.html')


def login(request):
    render(request,'accounts/login.html')


def logout(request):
    render(request,'accounts/logout.html')
