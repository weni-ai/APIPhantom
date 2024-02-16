from django.db import models

from apip.testplans.models import TestPlan


class Authenticator(models.Model):
    name = models.CharField(max_length=32)
    code = models.TextField()

    def __str__(self) -> str:
        return self.name


class TestCase(models.Model):
    title = models.CharField(max_length=255)
    testplan = models.ForeignKey(
        TestPlan, on_delete=models.CASCADE, related_name="test_cases"
    )
    code = models.TextField()
    authenticator = models.ForeignKey(
        Authenticator,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name="test_cases",
    )

    run_automatically = models.BooleanField(
        "Can run automatically",
        help_text="This field indicates whether this test case can be run automatically.",
        default=True,
    )

    def __str__(self) -> str:
        return self.title


class TestRun(models.Model):

    STATUS_RUNNING = "r"
    STATUS_PASS = "p"
    STATUS_FAILURE = "f"
    STATUS_ERROR = "e"

    STATUS_CHOICES = (
        (STATUS_RUNNING, "Running"),
        (STATUS_PASS, "Pass"),
        (STATUS_FAILURE, "Failure"),
        (STATUS_ERROR, "Error"),
    )

    test_case = models.ForeignKey(
        TestCase, on_delete=models.CASCADE, related_name="runs"
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    message = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        self.get_status_display()
        return f"{self.get_status_display()} - {self.test_case}"
