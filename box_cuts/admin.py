from django.contrib import admin
from .models import BoxCut


class BoxCutAdmin(admin.ModelAdmin):
    list_display = ["id", "total_ammount", "is_active",
                    "created_at", "user_made_cut", "box_openning"]


admin.site.register(BoxCut, BoxCutAdmin)
