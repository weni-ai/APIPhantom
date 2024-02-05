from django.contrib.admin.sites import AdminSite as DjangoAdminSite
from django.shortcuts import redirect


class AdminSite(DjangoAdminSite):
    site_header = "APIPhantom"
    site_title = "APIPhantom"

    def index(self, request, extra_context=None):
        return redirect("adminservices/service/")
