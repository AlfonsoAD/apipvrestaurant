from rest_framework import serializers
from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["id", "name", "description", "is_active", "created_at"]
        read_only_fields = ("id", "created_at")
