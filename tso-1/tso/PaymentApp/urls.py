from django.contrib import admin
from django.urls import path, include
from PaymentApp import views
from .views import *

urlpatterns = [
    path('upi/',views.UPIView,name='upi'),
    path('netbanking/',views.NetBankView,name='netbanking'),
    path('card/',views.CardView,name='card'),
]