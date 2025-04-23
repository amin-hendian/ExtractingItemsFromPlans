from django.http import JsonResponse
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from rest_framework.views import APIView

from .serilizers import PingResult, PingResultSerializer
from .tasks import first_celery_task


class PingApi(APIView):
    @swagger_auto_schema(responses={200: PingResultSerializer})
    def get(self, request):
        data = PingResult(time=timezone.now())
        response = PingResultSerializer(instance=data)
        return JsonResponse(response.data, status=200)
