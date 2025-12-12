from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import LershaUser

@admin.register(LershaUser)
class LershaUserAdmin(UserAdmin):
    # Show these fields in list view
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    
    # Fields when adding/editing
    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'phone_number', 'bio')}),
    #     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    #     ('Important dates', {'fields': ('last_login', 'date_joined')}),
    # )
    
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    
    ordering = ('email',)
