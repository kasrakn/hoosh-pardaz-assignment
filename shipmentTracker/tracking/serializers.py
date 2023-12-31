from rest_framework import serializers
from .models import Shipment

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = "__all__"


class ShipmentStatusSerializer(serializers.Serializer):
    tracking_number = serializers.CharField()
    carrier = serializers.CharField()