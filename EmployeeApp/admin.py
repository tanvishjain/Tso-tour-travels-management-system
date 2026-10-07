from django.contrib import admin
from EmployeeApp.models import *

# Register your models here.
class GuideAdmin(admin.ModelAdmin):
    list_display = ('id','First_Name','Middle_Name','Last_Name','Address_Line1','Address_Line2','City','Zip_Code','Phone_No','Emergency_Phone','Email','Gender')

    def get_queryset(self, request):
        Queryset = super(GuideAdmin, self).get_queryset(request)
        Queryset = Queryset.order_by('id')
        return Queryset

class DriverAdmin(admin.ModelAdmin):
    list_display = ('id','First_Name','Middle_Name','Last_Name','Address_Line1','Address_Line2','City','Zip_Code','Phone_No','Emergency_Phone','Email','License_Number','Gender')

    def get_queryset(self, request):
        Queryset = super(DriverAdmin, self).get_queryset(request)
        Queryset = Queryset.order_by('id')
        return Queryset

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','First_Name','Middle_Name','Last_Name','Address_Line1','Address_Line2','City','Phone_Number','Emergency_Phone','username','email','date_joined','Gender','Salary','Designation','Active_Status')

    def get_queryset(self, request):
        Queryset = super(EmployeeAdmin, self).get_queryset(request)
        Queryset = Queryset.order_by('id')
        return Queryset
    
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('id','Total_Amount','Net_Salary','Guide','Driver','Employee')

    def get_queryset(self, request):
        Queryset = super(SalaryAdmin, self).get_queryset(request)
        Queryset = Queryset.order_by('id')
        return Queryset

admin.site.register(Guide,GuideAdmin)
admin.site.register(Driver,DriverAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Salary,SalaryAdmin)