from typing import Any
from django.core.management.base import BaseCommand
from tracking.models import Shipment

class Command(BaseCommand):
    help = 'Populate the database with the initial data'

    def handle(self, *args: Any, **options: Any) -> None:
        with open('data.csv', 'r') as file:
            for line in file[1:]:
                cleaned_data = line.strip()
                data = cleaned_data.split(',')

                # Create model objects with the data
                Shipment.objects.create(
                    tracking_number=data[0],
                    carrier=data[1],
                    sender_address=data[2],
                    receiver_address=data[3],
                    article_name=data[4],
                    article_quantity=data[5],
                    article_price=data[6],
                    sku=data[7],
                    status=data[8]
                )
            self.stdout.write(self.style.SUCCESS('Initial data successfully populated'))