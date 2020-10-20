from django.contrib.auth.admin import admin, UserAdmin
from .models import Staff

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'staffID', 'is_active')

admin.site.register(Staff, CustomUserAdmin)
