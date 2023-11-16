from django.contrib import admin
from .models import Table


class TableAdmin(admin.ModelAdmin):
    list_display = ("id", "number", "capacity",
                    "table_status", "is_active", "created_at")


admin.site.register(Table, TableAdmin)
