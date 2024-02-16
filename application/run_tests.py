import traceback

import requests

from apip.services.models import Service
from apip.testplans.models import TestPlan
from apip.testcases.models import TestRun
from apip.testcases.models import TestCase
from . import test_runs


class Environments:
    def __repr__(self) -> str:
        return str(self.__dict__)


def setup_environments(service: Service) -> Environments:
    environments = Environments()
    for environment, value in service.environments.items():
        setattr(environments, environment, value)

    return environments


def run_test_case(test_case: TestCase, environments: Environments) -> TestRun:
    endpoint: TestPlan = test_case.testplan
    test_run: TestRun = test_runs.create(test_case)

    global_variables = {}

    def get_response(
        method, *args, endpoint: str = None, **kwargs
    ) -> requests.Response:
        url = environments.BASE_URL

        if endpoint is not None:
            url += endpoint

        headers = {}

        if test_case.authenticator is not None:
            exec(test_case.authenticator.code, global_variables)

            authenticator_class = global_variables.get("Authenticator")

            if authenticator_class is None:
                print("Authenticator dont declare the `Authenticate` class")

            authenticator = authenticator_class(environments)
            headers = authenticator.get_header()

        return requests.request(method, url, *args, headers=headers, **kwargs)

    try:
        exec(test_case.code)
        test_runs.set_status_pass(test_run)
    except AssertionError as error:
        test_runs.set_status_failure(test_run, str(error))
    except Exception as error:
        test_runs.set_status_error(test_run, traceback.format_exc())

    return test_run


def run_endpoint_tests(
    endpoint: TestPlan, environments: Environments, running_automatically: bool = False
) -> None:
    queryset = endpoint.test_cases.all()

    if running_automatically:
        queryset = queryset.filter(run_automatically=True)

    for test_case in queryset:
        run_test_case(test_case, environments)


def run_service_tests(service: Service, running_automatically: bool = False) -> None:
    environments = setup_environments(service)

    for endpoint in service.endpoints.all():
        run_endpoint_tests(endpoint, environments, running_automatically)


def run_all_tests(running_automatically: bool = False) -> None:
    for service in Service.objects.all():
        run_service_tests(service, running_automatically)
