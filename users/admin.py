from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = ("id", "email", "number_employee", "username",
                    "roles", "is_staff", "is_active")


admin.site.register(User, UserAdmin)
