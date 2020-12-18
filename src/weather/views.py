from rest_framework import viewsets, filters , mixins
from .models import Weather_data
from .serializer import WeatherSerializer
from rest_framework import generics
# Create your views here.

class WeatherViewSet(
                   mixins.RetrieveModelMixin, 
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Weather_data.objects.all().latest("date_time")
    serializer_class = WeatherSerializer