import requests
import json
from django.core.management.base import BaseCommand
from tracking.models import WeatherModel, ShipmentModel
from django.conf import settings

class Command(BaseCommand):
    help = 'Update weather information for all zip codes'

    def handle(self, *args, **kwargs):
        zipcodes = WeatherModel.objects.values_list('zipcode', flat=True)

        # A set to store cities
        city_set = set()

        # Get a list of unique receiver addresses
        receiver_queryset = ShipmentModel.objects.values_list('receiver_address', flat=True).distinct()

        # Extract the city codes and add them to the set
        for rq in receiver_queryset:
            address_parts = rq.split(",")
            city_set.add(address_parts[1].strip())

        for city in city_set:
            response = requests.get(
                url="http://api.weatherapi.com/v1/current.json",
                params={
                    "key": settings.WEATHER_API_KEY,
                    "q": city,
                    "aqi": "no"
                }
            )

            # Conver the response data to json
            json_data = json.loads(response.content)
            weather_object, created = WeatherModel.objects.get_or_create(
                zip_city=city
            )
            weather_object.temprature = json_data['current']['temp_c']
            weather_object.description = json_data['current']['condition']['text']
