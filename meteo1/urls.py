from django.urls import path
from meteo1.views import home_view

urlpatterns = [
    path('', home_view, name='home'),


]

