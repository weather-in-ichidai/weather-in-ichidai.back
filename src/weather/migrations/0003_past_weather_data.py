# Generated by Django 3.1.4 on 2021-01-01 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_remove_weather_data_clothing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Past_weather_data',
            fields=[
                ('date', models.DateTimeField(primary_key=True, serialize=False)),
                ('weather', models.CharField(max_length=20)),
                ('pop', models.IntegerField()),
                ('temp', models.CharField(max_length=200)),
            ],
        ),
    ]
