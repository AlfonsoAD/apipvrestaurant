from pvrestaurant.renderers import CustomJSONRenderer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import ProductNotes
from .serializers import ProductNotesSerializer
from pvrestaurant.permissions import IsWaiterRoleUser


class ProductNotesViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsWaiterRoleUser]
    serializer_class = ProductNotesSerializer
    queryset = ProductNotes.objects.all().filter(is_active=True)
    filter_backends = [DjangoFilterBackend]

    def destroy(self, request, *args, **kwargs):
        instance = ProductNotes.objects.get(pk=kwargs['pk'])
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_200_OK, data="Product Notes deleted successfully")
