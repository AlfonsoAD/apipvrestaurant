from pvrestaurant.renderers import CustomJSONRenderer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import DetailsMenu
from .serializers import DetailsMenuSerializer, DetailMenuReadSerializer
from pvrestaurant.permissions import IsAdminRoleUser


class DetailsMenuViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminRoleUser]
    serializer_class = DetailsMenuSerializer
    queryset = DetailsMenu.objects.all().filter(is_active=True)
    filter_backends = [DjangoFilterBackend]

    def destroy(self, request, *args, **kwargs):
        instance = DetailsMenu.objects.get(pk=kwargs['pk'])
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_200_OK, data="DetailsMenu deleted successfully")


class DetailsMenuAPIView(APIView):
    def get(self, request, idMenu):
        try:
            details_menu = DetailsMenu.objects.filter(
                menu=idMenu, is_active=True)
            serializer = DetailMenuReadSerializer(details_menu, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DetailsMenu.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
