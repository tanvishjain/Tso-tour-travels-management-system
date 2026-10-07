from django import forms
from django.forms import ModelForm
from .models import *

class UPIForm(ModelForm):
    class Meta:

        def __init__(self, user ,*args, **kwargs):
            super(UPIForm, self).__init__(*args, **kwargs)
            user_instance = user
            if user_instance:
                self.fields['User'].initial = user_instance

        model = UPI
        fields = ['UPI_Number']


class NetBankingForm(ModelForm):
    class Meta:

        def __init__(self, user ,*args, **kwargs):
            super(NetBankingForm, self).__init__(*args, **kwargs)
            user_instance = user
            if user_instance:
                self.fields['User'].initial = user_instance

        model = Net_Banking
        fields = ['Bank','username']

class CardForm(ModelForm):
    class Meta:

        def __init__(self, user ,*args, **kwargs):
            super(CardForm, self).__init__(*args, **kwargs)
            user_instance = user
            if user_instance:
                self.fields['User'].initial = user_instance

        model = Card
        fields = ['Card_Number','Expiry_Date','CVV']

        