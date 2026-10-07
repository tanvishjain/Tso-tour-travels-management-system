from django.contrib import admin
from .models import *

# Register your models here.
class PackageAdmin(admin.ModelAdmin):
    list_display=('id','Package_Name','Price','Posture','Starting_Date','Ending_Date','Duration','Available_Seats','Description','Registration_Deadline','Tour_Status','Inclusions','Exclusions','Offer','Discount_Percentage','State','Guide')

    def get_queryset(self, request):
        Queryset = super(PackageAdmin, self).get_queryset(request)
        Queryset = Queryset.order_by('id')
        return Queryset

class DayDescriptionAdmin(admin.ModelAdmin):
    list_display = ('id','Day_Number','Description','Package','Hotel','Vehicle','Rail','Flight','City')

    def get_queryset(self, request):
        Queryset = super(DayDescriptionAdmin, self).get_queryset(request)
        Queryset = Queryset.order_by('id')
        return Queryset

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id','Title','Image','Date_added','Package','Username')

    def get_queryset(self, request):
        Queryset = super(GalleryAdmin, self).get_queryset(request)
        Queryset = Queryset.order_by('id')
        return Queryset
    
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id','Hotel_Name','Address_Line1','Address_Line2','City','Zip_Code','Phone_No','Emergency_Phone','Email','Price_Per_Night','Hotel_Classification')

    def get_queryset(self, request):
        Queryset = super(HotelAdmin, self).get_queryset(request)
        Queryset = Queryset.order_by('id')
        return Queryset

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','Booking_DateTime','Total_Person','No_Of_Adults','No_Of_Children','Total_Amount','Payment_Mode','User','Package')

    def get_queryset(self, request):
        Queryset = super(BookingAdmin, self).get_queryset(request)
        Queryset = Queryset.order_by('id')
        return Queryset
    
class CancelAdmin(admin.ModelAdmin):
    list_display = ('id','Cancellation_DateTime','Reason','Cancellation_Fee','Refund_Amount','Booking')

    def get_queryset(self, request):
        Queryset = super(CancelAdmin, self).get_queryset(request)
        Queryset = Queryset.order_by('id')
        return Queryset

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id','Vehicle_Type','Registration_Number','Brand','Capacity','Fuel_Type','Insurance_Number','Vehicle_Category','Rental_Rate','Driver')

    def get_queryset(self, request):
        Queryset = super(VehicleAdmin, self).get_queryset(request)
        Queryset = Queryset.order_by('id')
        return Queryset
    
class FlightAdmin(admin.ModelAdmin):
    list_display = ('id','Airline_Name','Flight_Number','Available_Seats')

    def get_queryset(self, request):
        Queryset = super(FlightAdmin, self).get_queryset(request)
        Queryset = Queryset.order_by('id')
        return Queryset
    
class RailAdmin(admin.ModelAdmin):
    list_display = ('id','Train_Name','Available_Seats')

    def get_queryset(self, request):
        Queryset = super(RailAdmin, self).get_queryset(request)
        Queryset = Queryset.order_by('id')
        return Queryset
    
admin.site.register(Package,PackageAdmin)
admin.site.register(Day_Description,DayDescriptionAdmin)
admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Hotel,HotelAdmin)
admin.site.register(Booking,BookingAdmin)
admin.site.register(Cancellation,CancelAdmin)
admin.site.register(Vehicle,VehicleAdmin)
admin.site.register(Flight,FlightAdmin)
admin.site.register(Rail,RailAdmin)