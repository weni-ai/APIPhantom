from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf.urls.static import static
from django.conf import settings

from .health_check import HealthCheckView
from apip.testplans import urls as testplans_urls


urlpatterns = [
    path("", lambda service: redirect("adminservices/service/", permanent=True)),
    path(settings.HEALTH_CHECK_ENDPOINT, HealthCheckView.as_view()),
    path("admin", admin.site.urls),
    path("api/", include(testplans_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
