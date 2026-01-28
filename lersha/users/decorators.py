# Create a decorator to check if the user is logged in and is a farmer, if not redirect to the login page
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Farmer

def is_farmer(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
             if request.user.has_profile():
                return view_func(request, *args, **kwargs)
        return redirect('login-page')
    return wrapper

def is_subscribed(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.has_profile():
                if request.user.profile.is_active():
                    return view_func(request, *args, **kwargs)
        return redirect('subscribe-page')
    return wrapper