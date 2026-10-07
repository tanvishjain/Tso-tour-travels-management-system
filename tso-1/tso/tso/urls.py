"""
URL configuration for tso project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static
from Account.views import *
from home.views import *
from LocationApp.views import *
from EmployeeApp.views import *
from PackageApp.views import *
from PaymentApp.views import *

router = routers.DefaultRouter()
router.register(r'user',UserViewSet)
router.register(r'state',StateViewSet)
router.register(r'city',cityViewSet)
router.register(r'contact',ContactViewSet)
router.register(r'feedback',FeedbackViewSet)
router.register(r'guide',GuideViewSet)
router.register(r'driver',DriverViewSet)
router.register(r'employee',EmployeeViewSet)
router.register(r'salary',SalaryViewSet)
router.register(r'package',PackageViewSet)
router.register(r'hotel',HotelViewSet)
router.register(r'gallery',GalleryViewSet)
router.register(r'booking',BookingViewSet)
router.register(r'cancellation',CancelViewSet)
router.register(r'vehicle',VehicleViewSet)
router.register(r'flight',FlightViewSet)
router.register(r'rail',RailViewSet)
router.register(r'daydescription',DayViewSet)
router.register(r'UPI',UPIViewSet)
router.register(r'netbanking',NetBankingViewSet)
router.register(r'card',CardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('',include('home.urls')),
    path('signup/',include('Account.urls')),
    path('package/',include('PackageApp.urls')),
    path('payment/',include('PaymentApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
