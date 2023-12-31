from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Shipment
from .serializers import ShipmentSerializer

class ShipmentView(APIView):

    def get(self, request):
        queryset = Shipment.objects.all()
        serializer = ShipmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        return HttpResponseBadRequest()