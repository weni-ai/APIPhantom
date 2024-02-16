from django.contrib import admin
from django import forms

from apip.admin.widgets import get_ace_widget
from ..models import Authenticator


class AuthenticatorForm(forms.ModelForm):

    class Meta:
        model = Authenticator
        exclude = []
        widgets = {
            "code": get_ace_widget(),
        }


class AuthenticatorAdmin(admin.ModelAdmin):
    form = AuthenticatorForm
