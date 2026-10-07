from django.urls import path
from PackageApp import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('',views.PackageOverview,name='package-overview'),
    path('aft-package-overview',views.AfterPackageOverview,name='aft-package-overview'),
    path('package-detail/<id>/',views.PackageDetail,name='package-detail'),
    path('aft-package-detail/<id>/',views.AfterPackageDetail,name='aft-package-detail'),
    path('<id>/gallery-overview/',views.GalleryOverview,name='gallery-overview'),
    path('<id>/aft-gallery-overview/',views.AfterGalleryOverview,name='aft-gallery-overview'),
    path('gallery-detail/<Gallery_id>/',views.GalleryDetail,name='gallery-detail'),
    path('booking/',views.BookingView,name='booking'),
    path('cancellation/',views.CancelView,name='cancellation'),
    path('package-overview/gallery-detail/gallery-form/',views.GalleryView,name='gallery-form'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)