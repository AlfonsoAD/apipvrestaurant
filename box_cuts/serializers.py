from rest_framework import serializers
from .models import BoxCut
from users.serializers import UserSerializer
from box_oppenings.serializers import BoxOppeningSerializer


class BoxCutSerializer(serializers.ModelSerializer):
    user_made_cut = UserSerializer()
    box_openning = BoxOppeningSerializer()

    class Meta:
        model = BoxCut
        fields = ["id", "total_ammount", "is_active",
                  "created_at", "user_made_cut", "box_openning"]
        read_only_fields = ("id", "created_at",
                            "user_made_cut", "box_openning", )
