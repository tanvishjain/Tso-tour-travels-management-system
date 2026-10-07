from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    # list_display = ('id','First_Name','Middle_Name','Last_Name','Phone_Number','Emergency_Phone','username','email','date_joined','Gender','Address_Line1','Address_Line2','City','is_staff','is_active','is_superuser')
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('id','First_Name','Middle_Name','Last_Name','Phone_Number','Emergency_Phone','username','email','date_joined','Gender','Address_Line1','Address_Line2','City','is_staff','is_active','is_superuser')
    list_filter = ('id','is_staff','is_active','is_superuser')
    fieldsets = ((None,{'fields':('username','password')}),
                 ('Permissions',{'fields':('is_staff','is_active','is_superuser')}),)
    add_fieldsets = ((None,{'classes':('wide',),
                            'fields':('username','First_Name','Middle_Name','Last_Name','Phone_Number','Emergency_Phone','email','Gender','Address_Line1','Address_Line2','City','password1','password2','is_staff','is_active','is_superuser')}),)
    search_fields = ('username',)
    ordering = ('id',)

admin.site.register(CustomUser,CustomUserAdmin)