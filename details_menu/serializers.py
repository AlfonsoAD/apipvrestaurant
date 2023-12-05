from rest_framework import serializers
from .models import DetailsMenu
from menus.models import Menu
from menus.serializers import MenuSerializer
from products.models import Product
from products.serializers import ProductSerializer


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


class DetailMenuReadSerializer(serializers.ModelSerializer):
    menu = MenuSerializer()
    product = ProductSerializer()

    class Meta:
        model = DetailsMenu
        fields = ('id', 'is_active', 'created_at', 'menu', 'product')
