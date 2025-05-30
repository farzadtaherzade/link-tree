from . import views
from django.urls import path

urlpatterns = [
    path("link/", views.ListCreateApiView.as_view(),
         name="list-create-link-view"),
    path("link/<int:pk>/", views.RetrieveUpdateDestroy.as_view(),
         name="retrieve-update-destroy-link-view"),
    path("<str:username>/", views.DisplayLink.as_view(), name="display-links"),
]
