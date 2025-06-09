from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Link
from .serializers import LinkSerializers, DisplayLinkSerializers
from .permissions import IsOwner
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Profile

# Create your views here.


class ListCreateApiView(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = DisplayLinkSerializers
    permission_classes = [IsOwner, IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return LinkSerializers
        return DisplayLinkSerializers


class DisplayLink(generics.GenericAPIView):
    serializer_class = DisplayLinkSerializers

    def get(self, request, *args, **kwargs):
        username = kwargs.get("username")
        try:
            profile = Profile.objects.get(user__username=username)
            links = Link.objects.filter(
                user__username=username, is_active=True)
            serializer = self.get_serializer(
                {
                    'id': profile.id,
                    'avatar': profile.avatar,
                    'bio': profile.bio,
                    'display_name': profile.display_name,
                    'links': links  # Links are fetched via the user relationship
                })
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
