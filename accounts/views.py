from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):

    if request.method == 'POST':
        #User have info and want an account now
        if request.POST['password'] == request.POST['cpassword']:
            user = User.object.get(username = request.POST['username'])
            return render(request,'accounts/signup.html', {'error':'Username has already been taken'})
    else:
    #User wants to enter info


        return render(request,'accounts/signup.html')


def login(request):
    return render(request,'accounts/login.html')


def logout(request):
    return render(request,'accounts/signup.html')
# Create your views here.
