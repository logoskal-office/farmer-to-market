from django.urls import path
from .views import login_form, registration_form, logout_form
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', login_form, name='login'),
    path('logout/', logout_form, name='logout-page'),
    path('register/', registration_form, name='register'),
]