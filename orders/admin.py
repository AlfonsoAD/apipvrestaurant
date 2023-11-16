from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_number', 'date', 'process_status',
                    'priority', 'is_active', 'created_at', 'user', 'table',)


admin.site.register(Order, OrderAdmin)
