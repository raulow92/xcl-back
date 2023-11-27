from django.contrib.auth import get_user_model
from rest_framework import serializers
from wallets.models import Wallet

class WalletSerializer(serializers.ModelSerializer):
  class Meta:
    model = Wallet
    fields = ('balance_btc', 'balance_clp')