from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(
        max_length=255, 
        null=False
    )
    quantity = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    sku = models.CharField(null=False)

class Shipment(models.Model):
    IN_TRANSIT = "IT"
    INBOUND_SCAN = "IN"
    DELIVERY = "DL"
    TRANSIT = "TR"
    SCANNED = "SC"
    STATUS_CHOICES = {
        IN_TRANSIT: "in-transit",
        INBOUND_SCAN: "inbound-scan",
        DELIVERY: "delivery",
        TRANSIT: "transit",
        SCANNED: "scanned"
    }

    tracking_number = models.CharField(
        max_length=255, 
        unique=True
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
    status = models.CharField(
        max_length=2, 
        choices=STATUS_CHOICES, 
        default=IN_TRANSIT
        )
    article = models.ForeignKey(
        Article, 
        on_delete=models.CASCADE
        )
