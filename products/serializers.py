from rest_framework import serializers
from .models import Product
from categorys.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price',
                  'image', 'is_active', 'created_at', 'category']
        read_only_fields = ('id', 'created_at')
