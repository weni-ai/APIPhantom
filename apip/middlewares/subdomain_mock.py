from django.conf import settings
from django.http import Http404
from rest_framework.request import Request
from rest_framework.response import Response
from django.http import JsonResponse
from django.db.models import Q


from apip.testplans.models import Service, TestPlan
from apip.fackers import get_faker


def is_health_check_endpoint(request: Request):
    return bool(request.path == f"/{settings.HEALTH_CHECK_ENDPOINT}")


def get_request_subdomain(request: Request) -> str:
    if is_health_check_endpoint(request):
        return None

    host: str = request.get_host()

    host_parts = request.get_host().split(".")

    if host.startswith("127.0.0.1"):
        return None

    if len(host_parts) > len(settings.SERVICE_HOST.split(".")):
        return host_parts[0]

    return None


class SubdomainMockMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: Request) -> Response:
        subdomain = get_request_subdomain(request)

        if subdomain is None:
            return self.get_response(request)

        path = request.path

        if path == "/" or path == "/favicon.ico":
            raise Http404("Subdomínio não encontrado na URL")

        try:
            service = Service.objects.get(name__icontains=subdomain)
            
            test_plan = service.plans.filter(
                Q(endpoint=path) | 
                Q(endpoint__startswith=f"{path}?")
            ).first()
            
            if not test_plan:
                raise TestPlan.DoesNotExist("TestPlan não encontrado para o caminho")

            if test_plan.exact_value:
                return JsonResponse(test_plan.schema, status=200)

            fake_data = get_faker().generate_data_by_schema(test_plan.schema)
            return JsonResponse(fake_data, status=200)

        except Service.DoesNotExist:
            raise Http404("Serviço não encontrado para o subdomínio")

        except TestPlan.DoesNotExist:
            raise Http404("TestPlan não encontrado para o subdomínio")
