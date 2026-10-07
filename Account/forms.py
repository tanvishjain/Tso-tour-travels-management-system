from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm, UsernameField
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','First_Name','Middle_Name','Last_Name','Phone_Number','Emergency_Phone','email','Gender','Address_Line1','Address_Line2','City')
        # fields = '__all__'


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','First_Name','Middle_Name','Last_Name','Phone_Number','Emergency_Phone','email','Gender','Address_Line1','Address_Line2','City')
        # fields = '__all__'