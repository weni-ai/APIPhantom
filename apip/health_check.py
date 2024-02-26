from typing import TYPE_CHECKING

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

if TYPE_CHECKING:
    from rest_framework.request import Request


class HealthCheckView(APIView):

    authentication_classes = []

    def get(self, request: "Request") -> "Response":
        return Response({"up": True}, status=status.HTTP_200_OK)
