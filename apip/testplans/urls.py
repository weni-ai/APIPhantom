from django.urls import path

from .views import RunTestCase

urlpatterns = [
    path("run-testcase/<str:testcase>", RunTestCase.as_view(), name="run-testcase")
]
