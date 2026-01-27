from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
    return render(request, 'authentication/register.html')

@login_required
def logout_form(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'You have successfully logged out.')
        return redirect('home-page')
    return render(request, 'authentication/logout.html')
