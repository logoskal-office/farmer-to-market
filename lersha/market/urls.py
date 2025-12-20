from django.urls import path
from .views import *

urlpatterns = [
    path('products/', product_list, name='product-list-page'),
    path('products/<int:pk>/', product_detail, name='product-detail-page'),
    # path('pro')
]