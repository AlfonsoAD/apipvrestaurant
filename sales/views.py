from pvrestaurant.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Sale
from .serializers import SaleSerialiezer


class SaleViewSet(ModelViewSet):
    serializer_class = SaleSerialiezer
    queryset = Sale.objects.all().filter(is_active=True)
    filter_backends = [DjangoFilterBackend]

    def destroy(self, request, *args, **kwargs):
        instance = Sale.objects.get(pk=kwargs['pk'])
        instance.is_active = False
        instance.save()
        data = {"ok": True, "message": "Sale deleted successfully"}
        return Response(status=status.HTTP_200_OK, data=data)
