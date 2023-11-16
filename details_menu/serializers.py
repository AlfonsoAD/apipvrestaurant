from rest_framework import serializers
from .models import DetailsMenu


class DetailsMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailsMenu
        fields = ('id', 'is_active', 'created_at', 'menu', 'product')
        read_only_fields = ('id', 'created_at')
