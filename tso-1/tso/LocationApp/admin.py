from django.contrib import admin
from .models import *

# Register your models here.
class StateAdmin(admin.ModelAdmin):
    list_display = ('id','State_Name')

    def get_queryset(self, request):
        Queryset = super(StateAdmin, self).get_queryset(request)
        Queryset = Queryset.order_by('id')
        return Queryset
    
class CityAdmin(admin.ModelAdmin):
    list_display = ('id','City_Name','State')

    def get_queryset(self, request):
        Queryset = super(CityAdmin, self).get_queryset(request)
        Queryset = Queryset.order_by('id')
        return Queryset

admin.site.register(State,StateAdmin)
admin.site.register(City,CityAdmin)