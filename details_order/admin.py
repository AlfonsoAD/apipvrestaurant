from django.contrib import admin
from .models import DetailsOrder


class DetailsOrderAdmin(admin.ModelAdmin):
    list_display = ["id", 'articles_count', 'unit_price', 'order', 'product',
                    'is_active', 'created_at', 'updated_at']


admin.site.register(DetailsOrder, DetailsOrderAdmin)
