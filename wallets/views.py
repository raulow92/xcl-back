from django.shortcuts import render

# Create your views here.
from wallets.serializers import WalletSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from decimal import Decimal
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
  
class BuyView(APIView):
  def post(self, request, qty):
    qty = Decimal(qty)
    price_response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=clp")
    price = price_response.json()["bitcoin"]["clp"]
    user_wallet = request.user.wallet
    if user_wallet.balance_clp >= qty*price:
      user_wallet.balance_btc += qty
      user_wallet.balance_clp -= qty*price
      user_wallet.save()
      serializer = WalletSerializer(user_wallet)
      return Response(serializer.data)
    else:
      return Response(status=400)
    
class SellView(APIView):
  def post(self, request, qty):
    qty = Decimal(qty)
    price_response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=clp")
    price = price_response.json()["bitcoin"]["clp"]
    user_wallet = request.user.wallet
    if user_wallet.balance_btc >= qty:
      user_wallet.balance_btc -= qty
      user_wallet.balance_clp += qty*price
      user_wallet.save()
      serializer = WalletSerializer(user_wallet)
      return Response(serializer.data)
    else:
      return Response(status=400)