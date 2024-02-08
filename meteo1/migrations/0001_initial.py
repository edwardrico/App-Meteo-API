# Generated by Django 4.2.5 on 2024-01-18 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('humidity', models.IntegerField()),
                ('weather', models.CharField(max_length=100)),
                ('weather_description', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=2)),
                ('wind', models.FloatField()),
                ('wind_direction', models.IntegerField()),
            ],
        ),
    ]