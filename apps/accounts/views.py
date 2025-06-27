from django.shortcuts import render, redirect       
from django.contrib.auth.models import User       
from .forms import RegisterForm, ProfileForm, LoginForm       
from .models import Profile 
from django.contrib.auth import authenticate, login, logout


def register_view(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('login')
        
    else:
        user_form = RegisterForm()
        profile_form = ProfileForm()

    return render(request, 'register.html',{
        'user_form' : user_form,
        'profile_form' : profile_form
    })


def profile_view(request):
    return render(request, 'profile.html')

def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

            return redirect('profile')
        
        else:
            return render(request, 'login.html',{
                'login_form' : login_form,
                'error' : "Username yoki parol noto'g'ri!!!"
            })
        
    else:
        login_form = LoginForm()

    return render(request, 'login.html',{
        'login_form' : login_form
    })

def logout_view(request):
    logout(request)
    return redirect('login')

    