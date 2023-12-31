from typing import Any
import csv
from django.core.management.base import BaseCommand
from tracking.models import Shipment

class Command(BaseCommand):
    help = 'Populate the database with the initial data'

    def handle(self, *args: Any, **options: Any) -> None:
        with open('data.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0

            # loop over the rows of the csv file
            for row in csv_reader:
                if line_count != 0:

                    # Create model objects with the data
                    Shipment.objects.create(
                        tracking_number=row[0],
                        carrier=row[1],
                        sender_address=row[2],
                        receiver_address=row[3],
                        article_name=row[4],
                        article_quantity=row[5],
                        article_price=row[6],
                        sku=row[7],
                        status=row[8]
                    )
                    # Shipment.save()
                line_count += 1
            self.stdout.write(self.style.SUCCESS('Initial data successfully populated'))