from django.contrib.admin.sites import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_header = "APIPhantom"
    site_title = "APIPhantom"
