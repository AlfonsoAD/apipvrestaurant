from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Order
from .serializers import OrderSerializer


class DetailsOrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().filter(is_active=True)
    filter_backends = [DjangoFilterBackend]
