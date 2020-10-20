from django.contrib.auth.admin import admin
from .models import Staff

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'staffID')

admin.site.register(Staff, CustomUserAdmin)
