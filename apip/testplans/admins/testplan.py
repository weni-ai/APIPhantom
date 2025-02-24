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
        "redirect",
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
    
    def redirect(self, obj: TestPlan, request):
        protocol = 'https' if request.is_secure() else 'http'
        request_domain = request.get_host()

        url = f"{protocol}://{obj.service.subdomain}.{request_domain}{obj.endpoint}"
        
        html = f"""<a target="_blank" class="button" href="{url}" style="
                padding: 4px;
                display: flex;
                align-items: center;
                justify-content: center;
                width: fit-content;">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-box-arrow-up-right" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8.636 3.5a.5.5 0 0 0-.5-.5H1.5A1.5 1.5 0 0 0 0 4.5v10A1.5 1.5 0 0 0 1.5 16h10a1.5 1.5 0 0 0 1.5-1.5V7.864a.5.5 0 0 0-1 0V14.5a.5.5 0 0 1-.5.5h-10a.5.5 0 0 1-.5-.5v-10a.5.5 0 0 1 .5-.5h6.636a.5.5 0 0 0 .5-.5"/>
                <path fill-rule="evenodd" d="M16 .5a.5.5 0 0 0-.5-.5h-5a.5.5 0 0 0 0 1h3.793L6.146 9.146a.5.5 0 1 0 .708.708L15 1.707V5.5a.5.5 0 0 0 1 0z"/>
            </svg>
        </a>"""
        return format_html(html)

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

    def get_list_display(self, request):
        return [field if field != "redirect" else lambda obj: self.redirect(obj, request) for field in super().get_list_display(request)]

    run_tests.short_description = "Rodar testes"
