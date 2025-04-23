from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .authentication import UserAuthentication
from .serializers import ResultRequestSerializer, ResultResponseSerializer
from .tasks import decode_file_task

# Create your views here.


class FileUploadApi(APIView):
    authenticated_classes = [UserAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request=ResultRequestSerializer, response={200: ResultResponseSerializer}
    )
    def post(self, request):
        result_request = ResultRequestSerializer(data=request.data)
        result_model = result_request.save(user_id=request.user.id)
        decode_file_task.delay(result_model.id)
        result_response = ResultResponseSerializer(instance=result_model)
        return Response(result_response.data, status=200)
