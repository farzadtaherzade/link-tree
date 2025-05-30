from django.urls import path
from . import views

urlpatterns = [
    path("check/<str:username>/", views.SearchUsername.as_view(),
         name='search-available-username'),
    path("me/", views.ProfileRetrieve.as_view(), name="my-profile"),
]
