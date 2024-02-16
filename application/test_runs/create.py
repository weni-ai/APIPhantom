from apip.testcases.models import TestCase, TestRun


def create(endpoint: TestCase) -> TestRun:
    return TestRun.objects.create(test_case=endpoint, status=TestRun.STATUS_RUNNING)
