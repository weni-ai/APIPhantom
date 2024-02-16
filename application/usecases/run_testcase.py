from dataclasses import dataclass

from apip.testcases.models import TestCase
from .exceptions import TestCaseDoesNotExists

from ..run_tests import setup_environments, run_test_case


@dataclass
class TestCaseRun:
    status: str
    message: str


def run_testcase(testcase_id: int):
    try:
        testcase = TestCase.objects.get(id=testcase_id)
        environments = setup_environments(service=testcase.testplan.service)
        test_run = run_test_case(test_case=testcase, environments=environments)
        return TestCaseRun(
            status=test_run.get_status_display(), message=test_run.message
        )

    except TestCase.DoesNotExist as e:
        raise TestCaseDoesNotExists(e)
