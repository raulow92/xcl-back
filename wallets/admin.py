from django.contrib import admin

# Register your models here.
from wallets.models import Wallet

admin.site.register(Wallet)