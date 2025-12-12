from django.urls import path
from .views import home, about, contact

urlpatterns = [
    path('', home, name='landing-page'),
    path('home/', home, name='home-page'),
    path('about-us/', about, name='about-page'),
    path('contact-us/', contact, name='contact-page'),
]