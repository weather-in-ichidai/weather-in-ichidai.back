from django.db import models
import uuid

class Weather_data(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_time = models.DateTimeField()
    weather = models.CharField(max_length = 20)
    pop = models.IntegerField()
    temp = models.CharField(max_length = 200)
    now_rain = models.IntegerField()