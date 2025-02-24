from django import forms
from django.contrib import admin
from django.utils.html import format_html

from apip.testcases.admins.testcase import TestCaseInline
from apip.admin.widgets import get_ace_widget
from ..models import TestPlan


class TestPlanForm(forms.ModelForm):

    class Meta:
        exclude = []
        model = TestPlan
        widgets = {
            "schema": get_ace_widget(mode="json"),
        }


class TestPlanAdmin(admin.ModelAdmin):
    list_display = (
        "endpoint",
        "service",
        #"test_passing",
        #"run_tests",
    )
    list_filter = ["service"]
    search_fields = ["endpoint", "service__name"]
    inlines = [TestCaseInline]
    form = TestPlanForm

    def run_tests(self, endpoint):
        button_html = '<a class="button" href="">Rodar testes</a>'
        return format_html(button_html)

    def test_passing(self, endpoint: TestPlan):
        passing = True
        running = False

        if running:
            html = '<a class="button" href="">Running</a>'

        else:
            if not passing:
                html = '<a class="button" href="">Error</a>'
            else:
                html = '<a class="button" href="">Passing</a>'

        return format_html(html)

    run_tests.short_description = "Rodar testes"
