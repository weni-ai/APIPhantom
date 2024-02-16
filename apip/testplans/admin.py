from django.contrib import admin

from .models import TestPlan
from .admins import TestPlanAdmin


admin.site.register(TestPlan, TestPlanAdmin)
