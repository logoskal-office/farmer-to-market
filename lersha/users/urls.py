from django.urls import path
from .views import profile_update, profile, farmer_products_list, farmer_products_detail, farmer_product_delete, farmer_product_create

urlpatterns = [
    path('profile/', profile_update, name='profile-update-page'),
    path('profile/<int:pk>/', profile, name='profile-page'),
    path('profile/my-products', farmer_products_list, name='farmer-product-list'),
    path('profile/my-products/<int:pk>/', farmer_products_detail, name='farmer-product-detail'),
    path('product/<int:product_id>/delete/', farmer_product_delete, name='farmer-product-delete'),
    path('product/create/', farmer_product_create, name='farmer-product-create')
]