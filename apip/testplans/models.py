from django.db import models

from apip.services.models import Service


class TestPlan(models.Model):
    endpoint = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="plans")
    exact_value = models.BooleanField(
        "Exact Value",
        help_text="This field indicates that the value returned will be the same as that defined in schema",
        default=False
    )
    schema = models.JSONField(null=True, default=dict)

    def __str__(self) -> str:
        return self.endpoint
