from django.db import models

from apip.services.models import Service


class TestPlan(models.Model):
    endpoint = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="plans")
    schema = models.JSONField(null=True, default=dict)

    def __str__(self) -> str:
        return self.endpoint
