"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainSlidingView
from accounts.views import ProfileView
from wallets.views import ChartView, PriceView, WalletView, BuyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', TokenObtainSlidingView.as_view(), name='login'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('chart', ChartView.as_view(), name='chart'),
    path('price', PriceView.as_view(), name='price'),
    path('wallet', WalletView.as_view(), name='wallet'),
    path('buy/<str:qty>', BuyView.as_view(), name='buy'),
    # path('sell/<str:qty>', SellView.as_view(), name='sell'),
]
