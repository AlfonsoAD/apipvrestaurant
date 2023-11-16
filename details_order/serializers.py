from rest_framework import serializers
from .models import DetailsOrder
from orders.serializers import OrderSerializer
from products.serializers import ProductSerializer


class DetailsOrderSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    product = ProductSerializer()

    class Meta:
        model = DetailsOrder
        fields = ['id', 'articles_count', 'unit_price', 'is_active',
                  'created_at', 'updated_at', 'order', 'product',]
        read_only_fields = ('id', 'created_at',)
