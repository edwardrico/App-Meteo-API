from django.db import models


class Meteo(models.Model):
    temperature = models.FloatField()
    humidity = models.IntegerField()
    weather = models.CharField(max_length=100)
    weather_description = models.CharField(max_length=255)
    icon = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=2)
    wind = models.FloatField()
    wind_direction = models.IntegerField()

    def __str__(self):
        return f"Météo à {self.city}, {self.country}"
