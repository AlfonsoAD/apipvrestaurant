from rest_framework import serializers
from .models import Order
from users.models import User
from tables.models import Table


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all().filter(is_active=True)
    )
    table = serializers.PrimaryKeyRelatedField(
        queryset=Table.objects.all().filter(is_active=True))

    class Meta:
        model = Order
        fields = ['id', 'date', 'process_status',
                  'priority', 'is_active', 'created_at', 'updated_at', 'user', 'table',]
        read_only_fields = ('id', 'created_at',)
