from rest_framework import serializers
from .models import Sale
from orders.serializers import OrderSerializer


class SaleSerialiezer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = Sale
        fields = ["id", "created_at", "total_sale",
                  "is_active", "updated_at", "order"]
        read_only_fields = ["id", "created_at",]
