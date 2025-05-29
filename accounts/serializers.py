from rest_framework import serializers
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]
