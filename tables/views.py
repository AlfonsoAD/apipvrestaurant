from pvrestaurant.renderers import CustomJSONRenderer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Table
from .serializers import TableSerializer


class TableViewSet(ModelViewSet):
    serializer_class = TableSerializer
    queryset = Table.objects.all().filter(is_active=True)
    filter_backends = [DjangoFilterBackend]

    def destroy(self, request, *args, **kwargs):
        instance = Table.objects.get(pk=kwargs['pk'])
        instance.is_active = False
        instance.save()
        data = {"ok": True, "message": "Table deleted successfully"}
        return Response(status=status.HTTP_200_OK, data=data)
