from rest_framework import serializers
from .models import User
from handlers.user_handler import activate_role_user
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        data_user = [
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "roles": user.roles
            }
        ]
        token['user'] = data_user

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user or self.context['request'].user
        data_user = [
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "roles": user.roles
            }
        ]
        data['user'] = data_user

        return data


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "password",
                  "first_name", "last_name", "roles", "image"]

    # Función para encryptar el password con django
    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        # Activar is_superuser e is_staff del usuario si incluye el rol admin
        instance = activate_role_user(instance, validated_data["roles"])

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "first_name",
                  "last_name", "roles", "image"]


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "password"]
        read_only_fields = ("id", "email", "username",)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
