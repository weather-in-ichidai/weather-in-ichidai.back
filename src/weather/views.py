from rest_framework import viewsets, filters , mixins
from rest_framework.response import Response
from .models import Weather_data
from .serializer import WeatherSerializer
from rest_framework import generics
# Create your views here.

class WeatherViewSet(
                   mixins.RetrieveModelMixin, 
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    
    queryset = Weather_data.objects.all()
    serializer_class = WeatherSerializer

    def list(self,request):
        data = WeatherSerializer(Weather_data.objects.all().order_by("date_time").reverse().first()).data
        
        return Response(status=200 , data=data)