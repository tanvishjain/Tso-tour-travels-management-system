from django.contrib import admin
from home.models import Contact, Feedback

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','First_Name','Last_Name','Email','Phone_Number','Message')

    def get_queryset(self, request):
        Queryset = super(ContactAdmin, self).get_queryset(request)
        Queryset = Queryset.order_by('id')
        return Queryset
    
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id','Rating','Feedback','Date_Time')

    def get_queryset(self, request):
        Queryset = super(FeedbackAdmin, self).get_queryset(request)
        Queryset = Queryset.order_by('id')
        return Queryset

admin.site.register(Contact,ContactAdmin)   
admin.site.register(Feedback,FeedbackAdmin)