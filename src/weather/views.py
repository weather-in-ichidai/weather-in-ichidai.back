from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import management
from .models import Weather_data,Past_weather_data
from .serializer import WeatherSerializer,PastWeatherSerializer
from rest_framework.exceptions import ValidationError

import datetime
# Create your views here.

class WeatherViewSet(APIView):
    def get(self,request):
        req_date_str = self.request.query_params.get("date")
        if req_date_str is None:
            req_date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        req_date_t = datetime.datetime.strptime(req_date_str,"%Y-%m-%d")
        req_date = req_date_t.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=9)))
        if(req_date.date() == datetime.date.today()):
            queryset = Weather_data.objects.all()
            serializer_class = WeatherSerializer
            data = WeatherSerializer(Weather_data.objects.all().order_by("date_time").reverse().first()).data
            return Response(status=200 , data=data)
        elif(req_date.date() > datetime.date.today()):
            data = {"code":400,"message":"Invalid query parameter of date"}
            return Response(status=400 , data=data)
        else:
            queryset = Past_weather_data.objects.all().filter(date=req_date_str)
            serializer_class = PastWeatherSerializer
            data = ""
            if len(queryset) != 0:
                data = PastWeatherSerializer(queryset, many=True).data
            else:
                result = management.call_command('get_past_weather_from_POTEKA',date=req_date_str)
                queryset = Past_weather_data.objects.all().filter(date=req_date_str)
                data = PastWeatherSerializer(queryset, many=True).data
            return Response(status=200,data=data)