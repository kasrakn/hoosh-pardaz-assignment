from django.urls import path
from .views import ShipmentListView

urlpatterns = [
    path('shipment/', ShipmentListView.as_view(), name='shipment-list'),
]