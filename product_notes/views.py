from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import ProductNotes
from .serializers import ProductNotesSerializer


class ProductNotesViewSet(ModelViewSet):
    serializer_class = ProductNotesSerializer
    queryset = ProductNotes.objects.all().filter(is_active=True)
    filter_backends = [DjangoFilterBackend]
