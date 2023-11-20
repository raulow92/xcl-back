from django.db import models

# Create your models here.

class Wallet(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  balanceBTC = models.FloatField(default=0)
  balanceCLP = models.FloatField(default=0)