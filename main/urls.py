from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('secret/admin/', admin.site.urls),
    path('links/', include("links.urls")),
    path("accounts/", include("accounts.urls")),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
