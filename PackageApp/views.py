from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.contrib import messages
from .models import *
from .serializers import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user

# Create your views here.
class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = packageSerializer

# class DiscountViewSet(viewsets.ModelViewSet):
#     queryset = Discount.objects.all()
#     serializer_class = discountSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = hotelSerializer

class DayViewSet(viewsets.ModelViewSet):
    queryset = Day_Description.objects.all()
    serializer_class = daySerializer

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = guideSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer

class CancelViewSet(viewsets.ModelViewSet):
    queryset = Cancellation.objects.all()
    serializer_class = cancelSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = vehicleSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all() 
    serializer_class = flightSerializer

class RailViewSet(viewsets.ModelViewSet):
    queryset = Rail.objects.all()
    serializer_class = railSerializer

def PackageOverview(request):
    PackageData = Package.objects.filter(Tour_Status='Scheduled')
    context = {
        'PackageData':PackageData
    }
    return render(request,'PackageApp/package_overview.html',context)

def AfterPackageOverview(request):
    PackageData = Package.objects.filter(Tour_Status='Scheduled')
    context = {
        'PackageData':PackageData
    }
    return render(request,'PackageApp/after_login_package_overview.html',context)

def PackageDetail(request,id):
        PackageData = Package.objects.filter(id=id)
        DayData = Day_Description.objects.filter(Package=id)
        GalleryData = Gallery.objects.filter(Package=id)[:4]

        context ={
            'PackageData' : PackageData,
            'DayData' : DayData,
            'GalleryData' : GalleryData,
        }
        return render(request,'PackageApp/package_detail.html',context)

def AfterPackageDetail(request,id):
        PackageData = Package.objects.filter(id=id)
        DayData = Day_Description.objects.filter(Package=id)
        GalleryData = Gallery.objects.filter(Package=id)[:4]
        context ={
            'PackageData' : PackageData,
            'DayData' : DayData,
            'GalleryData' : GalleryData,
        }
        return render(request,'PackageApp/after_login_package_detail.html',context)

def GalleryOverview(request,id):
    GalleryData = Gallery.objects.filter(Package=id)
    PackageData = Package.objects.filter(id=id)
    return render(request,'PackageApp/gallery_overview.html',{'GalleryData' : GalleryData , 'PackageData' : PackageData})

def AfterGalleryOverview(request,id):
    GalleryData = Gallery.objects.filter(Package=id)
    PackageData = Package.objects.filter(id=id)
    return render(request,'PackageApp/aft_login_gallery_overview.html',{'GalleryData' : GalleryData , 'PackageData' : PackageData})

def GalleryDetail(request,Gallery_id):
    GalleryData = Gallery.objects.get()
    return render(request,'PackageApp/gallery_detail.html',{'GalleryData' : GalleryData})

@login_required(login_url='/log-page/')
def BookingView(request):
    user = request.user

    if request.method == 'POST':
        form = BookingForm(request.POST, user)
        if form.is_valid(): 
            booking = form.save()
            if booking.Payment_Mode == 'UPI':
                return redirect('/payment/upi/')
            elif booking.Payment_Mode == 'Net Banking':
                return redirect('/payment/netbanking/')
            else:
                # return render(request,'PaymentApp/card.html',{'booking_id' : booking_id})
                return redirect('/payment/card/')
    else:
        form = BookingForm()  
        # form = BookingForm()  

    context = {'form' : form}
    return render(request,'PackageApp/booking.html',context)

@login_required(login_url='/log-page/')
def CancelView(request):

    if request.method == 'POST':
        form = CancellationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home/after_login_index.html')
        
    else:
        form = CancellationForm()

    context = {'form' : form}
    return render(request,'PackageApp/cancel.html',context)

@login_required
def GalleryView(request):
    # user = request.user

    if request.method == 'POST':
        form = GalleryForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return render(request,'home/after_login_index.html')
        
    else:
        form = GalleryForm()

    context = {'form' : form}
    return render(request,'PackageApp/gallery.html',context)