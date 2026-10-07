from django.contrib import admin
from .models import *

# Register your models here.
class UPIAdmin(admin.ModelAdmin):
    list_display = ('id','UPI_Number','Package','User')

    def get_queryset(self, request):
        Queryset = super(UPIAdmin, self).get_queryset(request)
        Queryset = Queryset.order_by('id')
        return Queryset
    
class NetBankAdmin(admin.ModelAdmin):
    list_display = ('id','Bank','username','Package','User')

    def get_queryset(self, request):
        Queryset = super(NetBankAdmin, self).get_queryset(request)
        Queryset = Queryset.order_by('id')
        return Queryset
    
class CardAdmin(admin.ModelAdmin):
    list_display = ('id','Card_Number','Expiry_Date','Package','User')

    def get_queryset(self, request):
        Queryset = super(CardAdmin, self).get_queryset(request)
        Queryset = Queryset.order_by('id')
        return Queryset
    
admin.site.register(UPI,UPIAdmin)
admin.site.register(Net_Banking,NetBankAdmin)
admin.site.register(Card,CardAdmin)