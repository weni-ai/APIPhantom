from typing import TYPE_CHECKING

from rest_framework.response import Response
from rest_framework.views import APIView

if TYPE_CHECKING:
    from rest_framework.request import Request

from application.usecases import run_testcase
from application.usecases.exceptions import TestCaseDoesNotExists


class RunTestCase(APIView):

    authentication_classes = []  # TODO: Make auth

    def post(self, request: "Request", testcase: str) -> "Response":
        try:
            test_run = run_testcase(int(testcase))
        except TestCaseDoesNotExists as e:
            return Response(
                {"detail": "Test Run with id does't not exists"}, status=404
            )

        return Response({"status": test_run.status, "message": test_run.message})
