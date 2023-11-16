from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Menu
from .serializers import MenuSerializer


class MenuViewSet(ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all().filter(is_active=True)
    filter_backends = [DjangoFilterBackend]
