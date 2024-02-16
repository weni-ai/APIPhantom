from apip.testcases.models import TestRun


def set_status_running(test_run: TestRun):
    test_run.status = TestRun.STATUS_RUNNING
    test_run.save()


def set_status_pass(test_run: TestRun):
    test_run.status = TestRun.STATUS_PASS
    test_run.save()


def set_status_failure(test_run: TestRun, message: str):
    test_run.status = TestRun.STATUS_FAILURE
    test_run.message = message
    test_run.save()


def set_status_error(test_run: TestRun, message: str):
    test_run.status = TestRun.STATUS_ERROR
    test_run.message = message
    test_run.save()
