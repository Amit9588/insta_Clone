from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User  # Replace with your actual user model

class CustomUserAdmin(UserAdmin):
    # Customize how the user model is displayed in the admin interface
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']

# Register the custom user model with the custom admin class
admin.site.register(User, CustomUserAdmin)
