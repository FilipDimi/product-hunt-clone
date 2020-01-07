from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# TODO use regular expressions to prevent simple password!

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'account/signup.html', {"error": "This username is already taken."})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'account/signup.html', {"error": "Passwords must match."})
    else:
        return render(request, 'account/signup.html')


def login(request):
    return render(request, 'account/login.html')


def logout(request):
    return render(request, 'account/signup.html')