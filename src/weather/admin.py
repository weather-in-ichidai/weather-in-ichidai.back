from django.contrib import admin

from .models import Weather_data,Past_weather_data


@admin.register(Weather_data)
class WeatherDataAdmin(admin.ModelAdmin):
    pass

@admin.register(Past_weather_data)
class PastWeatherDataAdmin(admin.ModelAdmin):
    pass

