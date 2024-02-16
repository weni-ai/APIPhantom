import os

from django.conf import settings

from apip.testplans.models import Service, TestPlan, TestCase


def setup_default_test_case(test_plan: TestPlan) -> TestCase:
    test_case_path = os.path.join(
        settings.BASE_DIR, "application/test_plan/default_test_case"
    )
    with open(test_case_path, "r") as test_case_file:
        return TestCase.objects.create(
            endpoint=test_plan,
            title="Assert if the response matches with the schema",
            code=test_case_file.read(),
        )


def create_test_plan(endpoint: str, service: Service, schema: dict) -> TestPlan:
    test_plan = TestPlan.objects.create(
        endpoint=endpoint, service=service, schema=schema
    )
    setup_default_test_case(test_plan)

    return test_plan
