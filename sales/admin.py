from django.contrib import admin
from .models import Sale


class SaleAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "total_sale",
                    "is_active", "updated_at", "order"]


admin.site.register(Sale, SaleAdmin)
