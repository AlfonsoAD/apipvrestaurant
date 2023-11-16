from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "is_active", "created_at")


admin.site.register(Menu, MenuAdmin)
