from pvrestaurant.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import BoxCut
from .serializers import BoxCutSerializer
from pvrestaurant.permissions import IsAdminRoleUser


class BoxCutViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminRoleUser]
    serializer_class = BoxCutSerializer
    queryset = BoxCut.objects.all().filter(is_active=True)
    filter_backends = [DjangoFilterBackend]

    def destroy(self, request, *args, **kwargs):
        instance = BoxCut.objects.get(pk=kwargs['pk'])
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_200_OK, data="Box cut deleted successfully")
