from django.urls import path
from .views import ShipmentView

urlpatterns = [
    path('shipment/', ShipmentView.as_view(), name='shipment-list')
]