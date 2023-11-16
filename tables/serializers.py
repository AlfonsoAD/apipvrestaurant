from rest_framework import serializers
from .models import Table


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ["id", "number", "capacity", "table_status", "is_active"]
        read_only_fields = ("id", "created_at")
