from rest_framework import serializers
from .models import Product
from categorys.models import Category
from categorys.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all().filter(is_active=True))

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price',
                  'image', 'is_active', 'created_at', 'category']
