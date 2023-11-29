from django.db import models
from accounts.models import User
# Create your models here.

class Wallet(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  balance_btc = models.FloatField(default=0)
  balance_clp = models.FloatField(default=0)