from django.urls import path, include
from django.shortcuts import redirect
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from django.urls import re_path

from .health_check import HealthCheckView
from apip.testplans import urls as testplans_urls


urlpatterns = [
    path("", lambda service: redirect("adminservices/service/", permanent=True)),
    path(settings.HEALTH_CHECK_ENDPOINT, HealthCheckView.as_view()),
    path("admin", admin.site.urls),
    path("api/", include(testplans_urls)),
]


# Serving static files

urlpatterns.append(re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}))
