from rest_framework import serializers
from .models import DetailsOrder
from orders.serializers import OrderSerializer
from orders.models import Order
from products.serializers import ProductSerializer
from products.models import Product


class DetailsOrderSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all().filter(is_active=True))
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all().filter(is_active=True))

    class Meta:
        model = DetailsOrder
        fields = ['id', 'articles_count', 'unit_price', 'is_active',
                  'created_at', 'updated_at', 'order', 'product',]
        read_only_fields = ('id', 'created_at',)


class DetailsOrderSerializerAll(serializers.ModelSerializer):
    order_id = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all().filter(is_active=True))
    product = ProductSerializer()

    class Meta:
        model = DetailsOrder
        fields = "__all__"
