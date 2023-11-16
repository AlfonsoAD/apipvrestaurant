from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import DetailsMenu
from .serializers import DetailsMenuSerializer


class DetailsMenuViewSet(ModelViewSet):
    serializer_class = DetailsMenuSerializer
    queryset = DetailsMenu.objects.all().filter(is_active=True)
    filter_backends = [DjangoFilterBackend]
