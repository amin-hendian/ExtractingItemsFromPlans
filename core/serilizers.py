from dataclasses import dataclass
from datetime import datetime

from rest_framework_dataclasses.serializers import DataclassSerializer


@dataclass
class PingResult:
    time: datetime


class PingResultSerializer(DataclassSerializer):
    class Meta:
        dataclass = PingResult
