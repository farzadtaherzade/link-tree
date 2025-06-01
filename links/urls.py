from . import views
from django.urls import path

urlpatterns = [
    path("", views.ListCreateApiView.as_view(),
         name="list-create-link-view"),
    path("<int:pk>/", views.RetrieveUpdateDestroy.as_view(),
         name="retrieve-update-destroy-link-view"),
    path("display/<str:username>/",
         views.DisplayLink.as_view(), name="display-links"),
]
