from pvrestaurant.renderers import CustomJSONRenderer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Menu
from .serializers import MenuSerializer
from pvrestaurant.permissions import IsAdminRoleUser


class MenuViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminRoleUser]
    serializer_class = MenuSerializer
    queryset = Menu.objects.all().filter(is_active=True)
    filter_backends = [DjangoFilterBackend]

    def destroy(self, request, *args, **kwargs):
        instance = Menu.objects.get(pk=kwargs['pk'])
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_200_OK, data="Menu deleted successfully")
