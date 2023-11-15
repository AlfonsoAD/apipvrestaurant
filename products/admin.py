from django.contrib import admin
from .models import Product


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price",
                    "image", "is_active", "created_at", "category")


admin.site.register(Product, ProductsAdmin)
