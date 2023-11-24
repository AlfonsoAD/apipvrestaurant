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


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "number_employee", "email", "username", "first_name",
                  "last_name", "roles", "image", "is_active"]
        read_only_fields = ["is_active"]


class UserUpdatePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "password"]
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        instance.save()
        return instance
