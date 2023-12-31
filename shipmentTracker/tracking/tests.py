from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve, reverse_lazy
from .views import ShipmentListView
from .models import ShipmentModel

import json
# Create your tests here.

class TestUrls(SimpleTestCase):

    def test_shipment_list(self):
        url = reverse('shipment-list')
        self.assertEqual(resolve(url).func.view_class, ShipmentListView)


class TestModels(TestCase):

    def test_shipment_object_creation(self):
        ShipmentModel.objects.create(
            tracking_number='TN987654',
            carrier='test-carrier',
            sender_address='Street 2, Mashhad, Iran',
            receiver_address='Street 2, 2023 Tehran, Iran',
            article_name='Laptop',
            article_quantity=20,
            article_price=10000,
            status='DL'
        )
        ShipmentModel.objects.create(
            tracking_number='TN9876543',
            carrier='test-carrier',
            sender_address='Street 3, Mashhad, Iran',
            receiver_address='Street 3, 2023 Tehran, Iran',
            article_name='Laptop',
            article_quantity=200,
            article_price=100000,
            status='IT'
        )

        self.assertEqual(ShipmentModel.objects.count(), 2)


class TestViews(TestCase):

    def setup(self):
        client = Client()

    def test_shipment_list_GET(self):
        ship1 = ShipmentModel.objects.create(
            tracking_number='TN987654',
            carrier='test-carrier',
            sender_address='Street 2, Mashhad, Iran',
            receiver_address='Street 2, 2023 Tehran, Iran',
            article_name='Laptop',
            article_quantity=20,
            article_price=10000,
            status='DL'
        )
        ship2 = ShipmentModel.objects.create(
            tracking_number='TN9876543',
            carrier='test-carrier',
            sender_address='Street 3, Mashhad, Iran',
            receiver_address='Street 3, 2023 Tehran, Iran',
            article_name='Laptop',
            article_quantity=200,
            article_price=100000,
            status='IT'
        )
        ship3 = ShipmentModel.objects.create(
            tracking_number='TN9876543',
            carrier='test-carrier',
            sender_address='Street 3, Mashhad, Iran',
            receiver_address='Street 3, 2023 Tehran, Iran',
            article_name='Lamp',
            article_quantity=40,
            article_price=30,
            status='IT'
        )
        expected_data =  [
            {
                "tracking_number": "TN987654",
                "carrier": "test-carrier",
                "sender_address": "Street 2, Mashhad, Iran",
                "receiver_address": "Street 2, 2023 Tehran, Iran",
                "article_name": "Laptop",
                "article_quantity": 20,
                "article_price": 10000.0,
                "sku": "",
                "status": "DL",
                'weather': None
            },
            {
                "tracking_number": "TN9876543",
                "carrier": "test-carrier",
                "sender_address": "Street 3, Mashhad, Iran",
                "receiver_address": "Street 3, 2023 Tehran, Iran",
                "article_name": "Laptop",
                "article_quantity": 200,
                "article_price": 100000.0,
                "sku": "",
                "status": "IT",
                'weather': None
            },
            {
                "tracking_number": "TN9876543",
                "carrier": "test-carrier",
                "sender_address": "Street 3, Mashhad, Iran",
                "receiver_address": "Street 3, 2023 Tehran, Iran",
                "article_name": "Lamp",
                "article_quantity": 40,
                "article_price": 30.0,
                "sku": "",
                "status": "IT",
                'weather': None
            }
        ]

        url = reverse('shipment-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

        # Try to parse the response data as a JSON
        try:
            json_data = json.loads(response.content.decode('utf-8'))
        except:
            self.fail("Response content is not a valid JSON")
        
        self.assertEqual(json_data[0]['tracking_number'], 'TN987654')
        self.assertEqual(json_data[2]['article_price'], 30)

        self.assertJSONEqual(response.content.decode('utf-8'), expected_data)

    
    def test_shipment_list_POST(self):
        ship1 = ShipmentModel.objects.create(
            tracking_number='TN987654',
            carrier='test-carrier',
            sender_address='Street 2, Mashhad, Iran',
            receiver_address='Street 2, 2023 Tehran, Iran',
            article_name='Laptop',
            article_quantity=20,
            article_price=10000,
            status='DL'
        )
        ship2 = ShipmentModel.objects.create(
            tracking_number='TN9876543',
            carrier='test-carrier',
            sender_address='Street 3, Mashhad, Iran',
            receiver_address='Street 3, 2023 Tehran, Iran',
            article_name='Laptop',
            article_quantity=200,
            article_price=100000,
            status='IT'
        )
        ship3 = ShipmentModel.objects.create(
            tracking_number='TN9876543',
            carrier='test-carrier',
            sender_address='Street 3, Mashhad, Iran',
            receiver_address='Street 3, 2023 Tehran, Iran',
            article_name='Lamp',
            article_quantity=40,
            article_price=30,
            status='IT'
        )

        url = reverse('shipment-list')
        response = self.client.post(url, data={
            'tracking_number': ship2.tracking_number,
            'carrier': ship2.carrier
        })

        expected_data = [
            {
                "tracking_number": "TN9876543",
                "carrier": "test-carrier",
                "status": "IT"
            },
            {
                "tracking_number": "TN9876543",
                "carrier": "test-carrier",
                "status": "IT"
            }
        ]

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content.decode('utf-8'), expected_data)