from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Register your models here.
class CustomUserAdmin(UserAdmin):
  list_display = ['id', 'first_name', 'last_name', 'email', 'is_staff']

admin.site.register(User, CustomUserAdmin)