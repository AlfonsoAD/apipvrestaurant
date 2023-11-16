from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Table
from .serializers import TableSerializer


class TableViewSet(ModelViewSet):
    serializer_class = TableSerializer
    queryset = Table.objects.all().filter(is_active=True)
    filter_backends = [DjangoFilterBackend]
