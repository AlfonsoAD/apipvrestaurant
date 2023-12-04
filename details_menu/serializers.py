from rest_framework import serializers
from .models import DetailsMenu
from menus.models import Menu
from products.models import Product


class DetailsMenuSerializer(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(
        queryset=Menu.objects.all().filter(is_active=True))
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all().filter(is_active=True)
    )

    class Meta:
        model = DetailsMenu
        fields = ('id', 'is_active', 'created_at', 'menu', 'product')
        read_only_fields = ('id', 'created_at')
