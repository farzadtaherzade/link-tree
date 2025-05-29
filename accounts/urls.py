from django.urls import path
from . import views

urlpatterns = [
    path("<str:username>/", views.SearchUsername.as_view(),
         name='search-available-username')
]
