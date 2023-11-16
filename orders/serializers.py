from rest_framework import serializers
from .models import Order
from users.serializers import UserSerializer
from tables.serializers import TableSerializer


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    table = TableSerializer()

    class Meta:
        model = Order
        fields = ['id', 'date', 'process_status',
                  'priority', 'is_active', 'created_at', 'updated_at', 'user', 'table',]
        read_only_fields = ('id', 'created_at',)
