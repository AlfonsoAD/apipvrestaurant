from django.contrib import admin
from .models import ProductNotes


class ProductNotesAdmin(admin.ModelAdmin):
    list_display = ["id", 'note', 'details_order',
                    'is_active', 'created_at', 'updated_at']


admin.site.register(ProductNotes, ProductNotesAdmin)
