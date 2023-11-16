from django.contrib import admin
from .models import BoxOppening


class BoxOppeningAdmin(admin.ModelAdmin):
    list_display = ["id", "starting_ammount",
                    "is_active", "created_at", "user_authorized"]


admin.site.register(BoxOppening, BoxOppeningAdmin)
