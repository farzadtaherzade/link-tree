from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializers, ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Profile

# Create your views here.

User = get_user_model()


class SearchUsername(generics.GenericAPIView):
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        username = kwargs.get("username")
        try:
            user = User.objects.get(username=username)

            return Response({"available": False, "status": status.HTTP_200_OK})
        except User.DoesNotExist:
            # Todo: add logger
            pass

        return Response({"available": True, "status": status.HTTP_200_OK})


class ProfileRetrieve(generics.GenericAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = request.user
        try:
            profile = Profile.objects.get(user=user)
            serializer = self.get_serializer(profile, data=request.data).save()
            return Response(serializer.data)
        except Profile.DoesNotExist:
            print("test")
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, *args, **kwargs):
        user = request.user
        try:
            profile = Profile.objects.get(user=user)
            serializer = self.get_serializer(profile)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
