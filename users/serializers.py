from rest_framework import serializers
from .models import User
from handlers.user_handler import activate_role_user


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
                  "last_name", "roles", "image", "is_active", "is_superuser"]


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
