from pvrestaurant.renderers import CustomJSONRenderer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import DetailsOrder
from .serializers import DetailsOrderSerializer, DetailsOrderSerializerAll
from pvrestaurant.permissions import IsAdminRoleUser, IsWaiterRoleUser


class DetailsOrderViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsWaiterRoleUser]
    serializer_class = DetailsOrderSerializer
    queryset = DetailsOrder.objects.all().filter(is_active=True)
    filter_backends = [DjangoFilterBackend]

    def destroy(self, request, *args, **kwargs):
        instance = DetailsOrder.objects.get(pk=kwargs['pk'])
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_200_OK, data="Detail order deleted successfully")


class DetailOrderAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            detail_order = DetailsOrder.objects.filter(
                order=kwargs['order_id'], is_active=True)
            serializer = DetailsOrderSerializerAll(detail_order, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DetailsOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
