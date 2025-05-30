from rest_framework import serializers
from .models import Link
from accounts.serializers import UserSerializers


class LinkSerializers(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)

    class Meta:
        model = Link
        fields = "__all__"
        read_only_fields = ["user"]


class DisplayLinkSerializers(serializers.Serializer):

    links = LinkSerializers(many=True, read_only=True)
    avatar = serializers.ImageField()
    bio = serializers.CharField()
    display_name = serializers.CharField()
