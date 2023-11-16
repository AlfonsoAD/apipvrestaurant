from rest_framework import serializers
from .models import BoxOpening


class BoxOppeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxOpening
        fields = ["id", "starting_ammount", "is_active",
                  "created_at", "user_authorized"]
        read_only_fields = ("id", "created_at", "user_authorized")
