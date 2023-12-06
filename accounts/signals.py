from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from wallets.models import Wallet

@receiver(post_save, sender=User)
def welcome_bonus(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(balance_clp=50000, balance_btc=0, user=instance)
        