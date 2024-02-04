from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=32)
    environments = models.JSONField(default=dict)

    def __str__(self) -> str:
        return self.name

    @property
    def subdomain(self) -> str:
        return self.name.lower()
