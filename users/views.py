from pvrestaurant.renderers import CustomJSONRenderer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.serializers import CustomTokenObtainPairSerializer, UserRegisterSerializer, UserSerializer, UserUpdateSerializer, UsersSerializer
from .models import User
from pvrestaurant.permissions import IsAdminRoleUser
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # token_data = serializer.validated_data
            user = serializer.user

            data_user = [
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "roles": user.roles
                }
            ]
            response.data['user'] = data_user

            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterView(APIView):
    permission_classes = [IsAuthenticated, IsAdminRoleUser]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):  # Si el serializer es valido
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = [IsAuthenticated, IsAdminRoleUser]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminRoleUser]
    serializer_class = UsersSerializer
    queryset = User.objects.all().filter(is_active=True)
    filter_backends = [DjangoFilterBackend]

    def destroy(self, request, *args, **kwargs):
        instance = User.objects.get(pk=kwargs["pk"])
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_200_OK, data="User deleted successfully")
