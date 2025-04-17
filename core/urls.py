from django.urls import URLPattern, path

from .views import PingApi

urlpatterns: list[URLPattern] = [path("ping", PingApi.as_view())]
