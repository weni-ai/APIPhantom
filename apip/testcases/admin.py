from django.contrib import admin

from .models import TestRun, Authenticator, TestCase
from .admins import AuthenticatorAdmin, TestCaseAdmin

admin.site.register(TestRun)
admin.site.register(Authenticator, AuthenticatorAdmin)
admin.site.register(TestCase, TestCaseAdmin)
