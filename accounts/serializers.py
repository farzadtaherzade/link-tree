from rest_framework import serializers
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ["user"]


class UserSerializers(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "username", 'profile']
        read_only_fields = ["email", "first_name", "last_name", 'profile']
