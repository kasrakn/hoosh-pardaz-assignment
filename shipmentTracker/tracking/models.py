from django.db import models


class ShipmentModel(models.Model):
    IN_TRANSIT = "IT"
    INBOUND_SCAN = "IN"
    DELIVERY = "DL"
    TRANSIT = "TR"
    SCANNED = "SC"
    STATUS_CHOICES = [
        (IN_TRANSIT, "in-transit"),
        (INBOUND_SCAN, "inbound-scan"),
        (DELIVERY, "delivery"),
        (TRANSIT, "transit"),
        (SCANNED, "scanned")
    ]

    tracking_number = models.CharField(
        max_length=255, 
        null=False
        )
    carrier = models.CharField(
        max_length=255, 
        null=False
        )
    sender_address = models.CharField(
        max_length=255, 
        null=False
        )
    receiver_address = models.CharField(
        max_length=255, 
        null=False
        )
    article_name = models.CharField(
        max_length=255, 
        null=False
    )
    article_quantity = models.IntegerField(null=False)
    article_price = models.FloatField(null=False)
    sku = models.CharField(max_length=255, null=False)
    status = models.CharField(
        max_length=2, 
        choices=STATUS_CHOICES, 
        default=IN_TRANSIT
        )

class WeatherModel(models.Model):
    zip_city = models.CharField(max_length=255)
    temprature = models.FloatField(null=True)
    description = models.CharField(max_length=20, null=True)