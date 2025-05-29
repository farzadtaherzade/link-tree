from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

User = get_user_model()


class SearchUsername(generics.GenericAPIView):
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        username = kwargs.get("username")
        try:
            user = User.objects.get(username=username)

            return Response({"available": False})
        except User.DoesNotExist:
            # Todo: add logger
            pass

        return Response({"available": True})
