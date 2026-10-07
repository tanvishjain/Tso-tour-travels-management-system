from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Booking, Cancellation, Gallery, Package

class BookingForm(ModelForm):
    class Meta:

        def __init__(self, user ,*args, **kwargs):
            super(BookingForm, self).__init__(*args, **kwargs)
            user_instance = user
            if user_instance:
                self.fields['User'].initial = user_instance.id

        model = Booking
        fields = ('Package','Total_Person','No_Of_Adults','No_Of_Children','Payment_Mode')


        def clean(self):
            Total_Person = self.cleaned_data['Total_Person']

            if Total_Person <= 0:
                raise forms.ValidationError('Person must be greater than 0.')
            return Total_Person
        
class CancellationForm(ModelForm):
    class Meta:
        model = Cancellation
        fields = ('Reason','Booking')

class GalleryForm(ModelForm):
    class Meta:
                   
        model = Gallery
        fields = ('Title','Image','Username','Package')
 
