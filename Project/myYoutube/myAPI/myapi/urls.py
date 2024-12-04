# myapi/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("users.urls")),  # Include users app URLs
    path("", lambda request: JsonResponse({"message": "Welcome to MyYouTube API"})),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
