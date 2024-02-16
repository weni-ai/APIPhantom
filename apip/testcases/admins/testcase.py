from django.contrib import admin
from django import forms
from django.db import models
from django_ace import AceWidget

from apip.services.models import Service
from apip.admin.widgets import get_ace_widget
from ..models import TestCase


class TestCaseForm(forms.ModelForm):

    class Meta:
        model = Service
        exclude = []
        widgets = {
            "code": AceWidget(
                mode="python",
                theme="twilight",
                width="100%",
                height="300px",
            ),
            "authenticator": forms.Select(attrs={"required": False}),
        }


class TestCaseAdmin(admin.ModelAdmin):
    form = TestCaseForm


class TestCaseInline(admin.StackedInline):
    model = TestCase
    extra = 0

    template = "testcase_inline.html"

    formfield_overrides = {
        models.TextField: {"widget": get_ace_widget()},
    }

    classes = ["collapse"]
