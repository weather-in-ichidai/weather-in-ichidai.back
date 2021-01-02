from rest_framework import serializers

from .models import Weather_data,Past_weather_data

class WeatherSerializer(serializers.ModelSerializer):
    minTemp = serializers.SerializerMethodField()
    maxTemp = serializers.SerializerMethodField()
    clothing = serializers.SerializerMethodField()
    rainfallRate = serializers.IntegerField(source = "pop")
    weatherType = serializers.CharField(source = "weather")
    temperature = serializers.CharField(source = "temp")

    description = serializers.SerializerMethodField()

    class Meta:
        model = Weather_data
        fields = ('date_time','weatherType','rainfallRate',"temperature","minTemp","maxTemp","clothing",'description')
    
    def get_minTemp(self,instance):
        minTemp = min(instance.temp.split(","))

        return minTemp

    def get_maxTemp(self,instance):
        maxTemp = max(instance.temp.split(","))

        return maxTemp

    def get_clothing(self,instance):
        minTemp = float(min(instance.temp.split(",")))
        if(minTemp<8):
            return "superCool"

        if(minTemp<13):
            return "cool"
        
        if(minTemp<20):
            return "common"
        if(minTemp<28):
            return "warm"
        return "superWarm"
        
    def get_description(self,instance):
        res_text = ""
        if(instance.now_rain == 0):
            res_text = "現在雨は降っていません"
        else:
            res_text = "現在雨が降っています"
        return res_text



class PastWeatherSerializer(serializers.ModelSerializer):
    weatherType = serializers.CharField(source = "weather")
    temperature = serializers.CharField(source = "temp")
    class Meta:
        model = Past_weather_data
        fields = ('date','weatherType','humi',"temperature")