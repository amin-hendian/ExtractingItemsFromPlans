from celery import shared_task

from .helper.pdfToImage import Decoded
from .models import FileUpload


@shared_task
def decode_file_task(result_id: int):
    uploaded_file = FileUpload.objects.get(id=result_id)
    file = uploaded_file.file.path()
    result = Decoded(file)
    uploaded_file.url_list = result.url_list
    uploaded_file.save()
