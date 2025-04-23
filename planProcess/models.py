from django.db import models

from core.models import User

# Create your models here.


class FileUpload(models.Model):
    file = models.FileField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    url_list = models.ExpressionList()
