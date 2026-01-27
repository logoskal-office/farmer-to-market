from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import LershaUser
from users.models import Farmer

def login_form(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome Back {user.first_name}")
                return redirect('profile-update-page')

        messages.error(request, 'Invalid credentials')
    return render(request, 'authentication/login.html')

def registration_form(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(1)
        if form.is_valid():
            print('form is valid')
            user = form.save()
            Farmer.objects.create(account=user)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, f"Welcome {user.first_name}")
            return redirect('profile-update-page')
        else:
            print(form.errors)
            messages.error(request, f'Error, {form.errors.as_text()}')
    return render(request, 'authentication/register.html')

@login_required
def logout_form(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'You have successfully logged out.')
        return redirect('home-page')
    return render(request, 'authentication/logout.html')

def login_choice(request):
    return render(request, 'authentication/login-choice.html')