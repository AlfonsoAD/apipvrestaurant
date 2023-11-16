from django.contrib import admin
from .models import DetailsMenu


class DetailsMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu', 'product', 'is_active', 'created_at',)


admin.site.register(DetailsMenu, DetailsMenuAdmin)
