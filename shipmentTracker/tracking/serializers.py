from rest_framework import serializers
from .models import Shipment

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ['tracking_number', 'carrier', 'sender_address', 
                  'receiver_address', "article_name", 'article_quantity',
                    'article_price', 'sku', 'status'
                    ]


class ShipmentStatusSerializer(serializers.Serializer):
    tracking_number = serializers.CharField()
    carrier = serializers.CharField()