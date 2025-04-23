from rest_framework import serializers

from .models import FileUpload


class ResultRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ["file"]


class ResultResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = "__all__"
