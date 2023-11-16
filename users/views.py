from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from .models import User


class UserRegisterView(APIView):

    # Para registrar un usuario
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):  # Si el serializer es valido
            serializer.save()
            data = {"ok": True, "message": "User created successfully",
                    "results": serializer.data}
            return Response(status=status.HTTP_201_CREATED, data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados

    def get(self, request):
        serializer = UserSerializer(request.user)
        data = {"ok": True, "results": serializer.data}
        return Response(status=status.HTTP_200_OK, data=data)

    def put(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {"ok": True, "message": "User updated successfully",
                    "results": serializer.data}
            return Response(status=status.HTTP_200_OK, data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
