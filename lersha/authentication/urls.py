from django.urls import path
from .views import login_form, registration_form, logout_form, login_choice

urlpatterns = [
    path('login/', login_form, name='login-page'),
    path('logout/', logout_form, name='logout-page'),
    path('register/', registration_form, name='register-page'),
    path('login-choice/', login_choice, name='login-choice-page'),
]