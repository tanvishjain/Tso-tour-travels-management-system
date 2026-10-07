from django.shortcuts import render
from django.contrib import messages 
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from .models import *
from .serializers import *
from .forms import *

# Create your views here.
class UPIViewSet(viewsets.ModelViewSet):
    queryset = UPI.objects.all()
    serializer_class = upiSerializer

class NetBankingViewSet(viewsets.ModelViewSet):
    queryset = Net_Banking.objects.all()
    serializer_class = netbankingSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = cardSerializer

def UPIView(request):
    user = request.user.username
    if request.method == 'POST':
        form = UPIForm(request.POST, user)
        if form.is_valid():
            form.save()
            return render(request,'home/after_login_index.html')
        
    else:
        form = UPIForm()

    context = {'form' : form}
    return render(request,'PaymentApp/upi.html',context)

def NetBankView(request):
    user = request.user.username
    if request.method == 'POST':
        form = NetBankingForm(request.POST,  user)
        if form.is_valid():
            form.save()
            return render(request,'home/after_login_index.html')
        
    else:
        form = NetBankingForm()

    context = {'form' : form}
    return render(request,'PaymentApp/netbanking.html',context)

def CardView(request):
    user = request.user.username
    if request.method == 'POST':
        form = CardForm(request.POST, user)
        if form.is_valid():
            form.save()
            return render(request,'home/after_login_index.html')
        
    else:
        form = CardForm()

    context = {'form' : form}
    return render(request,'PaymentApp/card.html',context)