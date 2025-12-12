from django.contrib import admin
from .models import Category, Product, Impression

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'active', 'date_listed')
    list_filter = ('active', 'category')
    search_fields = ('name', 'description')
    autocomplete_fields = ('category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Impression)
