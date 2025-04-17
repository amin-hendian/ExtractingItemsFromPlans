from django.http import JsonResponse
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from rest_framework.views import APIView

from .serilizers import PingResult, PingResultSerializer
from .tasks import first_celery_task


class PingApi(APIView):
    @swagger_auto_schema(response={200: PingResultSerializer()})
    def get(self, _: Request):
        data = PingResult(time=timezone.now())
        response = PingResultSerializer(instance=data)
        first_celery_task.delay(20)
        return JsonResponse(response, status=200)
