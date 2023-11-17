from rest_framework import serializers
from .models import BoxOppening


class BoxOppeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxOppening
        fields = ["id", "starting_ammount", "is_active",
                  "created_at", "user_authorized"]
        read_only_fields = ("id", "created_at", "user_authorized")
