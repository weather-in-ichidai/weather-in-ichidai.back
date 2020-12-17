from django.contrib import admin

from .models import Weather_data


@admin.register(Weather_data)
class WeatherDataAdmin(admin.ModelAdmin):
    pass
