from django.db import models
from PackageApp.models import Booking,Package
from Account.models import CustomUser
from datetime import datetime

# Create your models here.
class UPI(models.Model):
    UPI_Number = models.CharField(
        max_length = 50
    )
    Package = models.ForeignKey(
        Package,
        on_delete = models.CASCADE,
        default = 1
    )
    User = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,
        default = 1
    )

class Net_Banking(models.Model):
    Bank = models.CharField(
        max_length = 50,
        choices = (
            ('Bank of Baroda' , 'Bank of Baroda'),
            ('HDFC Bank' , 'HDFC Bank'),
            ('SBI Bank' , 'SBI Bank'),
            ('Punjab National Bank' , 'Punjab National Bank'),
            ('Union Bank of India' , 'Union Bank of India'),
            ('Axis Bank' , 'Axis Bank'),
            ('Bank of India' , 'Bank of India'),
            ('Canara Bank' , 'Canara Bank'),
            ('Indian Bank' , 'Indian Bank'),
            ('UCO Bank' , 'UCO Bank')
        )
    )
    username = models.CharField(
        max_length = 50
    )
    Package = models.ForeignKey(
        Package,
        on_delete = models.CASCADE,
        default = 1
    )
    User = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,
        default = 1
    )

# class MonthYearField(models.DateField):
#     def __init__(self, *args, **kwargs):
#         kwargs['null'] = True
#         kwargs['blank'] = True
#         super().__init__(*args, **kwargs)

#     def to_python(self, value):
#         if isinstance(value, str):
#             return value
#         elif isinstance(value, datetime.date):
#             return value.strftime('%Y-%m')
#         return value
    
#     def get_prep_value(self, value):
#         if value is None:
#             return None
#         return value.strftime('%Y-%m')
    
#     def from_db_value(self, value, expression, connection):
#         return self.to_python(value)

class Card(models.Model):
    Card_Number = models.CharField(
        max_length = 16
    )
    Expiry_Date = models.DateField()
    CVV = models.CharField(
        max_length = 3,
    )
    Package = models.ForeignKey(
        Package,
        on_delete = models.CASCADE,
        default = 1
    )
    User = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,
        default = 1
    )
       
