from django.contrib import admin
from django import forms

from .models import Service
from apip.admin.widgets import get_ace_widget


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        exclude = []
        widgets = {
            "environments": get_ace_widget("json"),
        }


class ServiceAdmin(admin.ModelAdmin):
    form = ServiceForm
    list_display = ("name",)


admin.site.register(Service, ServiceAdmin)
