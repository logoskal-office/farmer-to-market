from django.urls import path, include
from .views import chapa, chapa_callback_url_reciever, chapa_return_reciever

urlpatterns = [
    path('chapa/', chapa),
    path('chapa-response/', chapa_callback_url_reciever),
    path('chapa-return/', chapa_return_reciever),
    ]