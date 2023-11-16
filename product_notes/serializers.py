from rest_framework import serializers
from .models import ProductNotes
from details_order.serializers import DetailsOrderSerializer


class ProductNotesSerializer(serializers.ModelSerializer):
    details_order = DetailsOrderSerializer()

    class Meta:
        model = ProductNotes
        fields = ['id', 'note', 'is_active',
                  'created_at', 'updated_at', 'details_order',]
        read_only_fields = ('id', 'created_at',)
