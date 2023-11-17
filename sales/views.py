from pvrestaurant.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from .models import Sale
from .serializers import SaleSerialiezer
from pvrestaurant.permissions import IsCashierRoleUser


class SaleViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsCashierRoleUser]
    serializer_class = SaleSerialiezer
    queryset = Sale.objects.all().filter(is_active=True)
    filter_backends = [DjangoFilterBackend]

    def destroy(self, request, *args, **kwargs):
        instance = Sale.objects.get(pk=kwargs['pk'])
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_200_OK, data="Sale deleted successfully")
