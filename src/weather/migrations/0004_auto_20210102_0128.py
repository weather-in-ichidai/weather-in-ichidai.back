# Generated by Django 3.1.4 on 2021-01-01 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_past_weather_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='past_weather_data',
            old_name='pop',
            new_name='humi',
        ),
    ]