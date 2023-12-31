from rest_framework import serializers
from .models import ShipmentModel, WeatherModel

class ShipmentSerializer(serializers.ModelSerializer):
    weather =  serializers.SerializerMethodField()
    class Meta:
        model = ShipmentModel
        fields = ['tracking_number', 'carrier', 'sender_address', 
                  'receiver_address', "article_name", 'article_quantity',
                    'article_price', 'sku', 'status', 'weather'
                    ]
    
    def get_weather(self, instance):
        # Get the weather based on the receiver_address
        weather_instance = WeatherModel.get_weather_for_address(instance.receiver_address)

        # If weather is found, return the temperature
        if weather_instance:
            return str(weather_instance)
        else:
            return None


class ShipmentStatusSerializer(serializers.Serializer):
    tracking_number = serializers.CharField()
    carrier = serializers.CharField()