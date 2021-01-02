from .views import WeatherViewSet
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    url(r"^weather",WeatherViewSet.as_view())
]