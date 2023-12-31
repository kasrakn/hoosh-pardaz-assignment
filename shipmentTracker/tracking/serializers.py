from rest_framework import serializers
from .models import ShipmentModel

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentModel
        fields = ['tracking_number', 'carrier', 'sender_address', 
                  'receiver_address', "article_name", 'article_quantity',
                    'article_price', 'sku', 'status'
                    ]


class ShipmentStatusSerializer(serializers.Serializer):
    tracking_number = serializers.CharField()
    carrier = serializers.CharField()