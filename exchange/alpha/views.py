from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ExchangeRate
from django.core import serializers
from .worker import Worker
# from .serializers import RateSerializer
# Create your views here.


@api_view(['GET', 'POST'])
def exchange_rate(request):
    if request.method == 'GET':
        rates = ExchangeRate.objects.all()
        return Response(serializers.serialize('json',rates),status=status.HTTP_200_OK)
    elif request.method == 'POST':
        worker = Worker()
        worker.exchange()
        return Response(message="Done", status=status.HTTP_200_OK)
    else:
        return Response(message="ERROR: method not found", status=status.HTTP_400_BAD_REQUEST)