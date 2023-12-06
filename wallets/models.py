from django.db import models
from accounts.models import User
# Create your models here.

class Wallet(models.Model):
  balance_clp = models.DecimalField(default=0, max_digits=20, decimal_places=2)
  balance_btc = models.DecimalField(default=0, max_digits=20, decimal_places=8)
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.user.username}'s Wallet"
