from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Shipment
from .serializers import ShipmentSerializer, ShipmentStatusSerializer

class ShipmentListView(APIView):

    def get(self, request):
        queryset = Shipment.objects.all()
        serializer = ShipmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShipmentStatusSerializer(data=request.data)
        if serializer.is_valid():
            tracking_number = serializer.validated_data['tracking_number']
            carrier = serializer.validated_data['carrier']

            # Get the shipment objects with the given tracking number and carrier
            queryset = Shipment.objects.filter(
                tracking_number=tracking_number, 
                carrier=carrier
                )
            
            if len(queryset) == 0:
                return Response(serializer.errors, status=404)
            
            response_data = []

            # Loop over the found shipment objects and add their data to the response data
            for sh_obj in queryset:
                response_data.append(
                    {
                        'status': sh_obj.status,
                        'tracking_number': tracking_number,
                        'carrier': carrier
                    }
                )
            return Response(response_data)
                
    