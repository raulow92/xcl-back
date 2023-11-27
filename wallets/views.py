from django.shortcuts import render

# Create your views here.
from wallets.serializers import WalletSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class ChartView(APIView):
  def get(self, request):
    chart = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=clp&days=90')
    return Response(chart.json())

class PriceView(APIView):
  def get(self, request):
    price = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=clp')
    return Response(price.json())

class WalletView(APIView):
  def get(self, request):
    current_user = request.user
    wallet = current_user.wallet
    serializer = WalletSerializer(wallet)
    return Response(serializer.data)