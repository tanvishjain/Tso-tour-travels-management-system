from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.
class CustomUser(AbstractUser):

    first_name = None
    last_name = None
    id = models.AutoField(
        primary_key=True,
        auto_created=True
    )
    First_Name = models.CharField(
        max_length = 50,
    )
    Last_Name = models.CharField(
        max_length = 50,
    )
    Middle_Name = models.CharField(
        max_length = 50,
    )
    Phone_Number = models.CharField(
        max_length = 10
    )
    Emergency_Phone = models.CharField(
        max_length = 10
    )
    Gender = models.CharField(
        max_length = 1,
        choices = (
            ('M' , 'Male'),
            ('F' , 'Female'),
            ('O' , 'Other')
        ),
    )
    Address_Line1 = models.CharField(
        max_length = 100,
    )
    Address_Line2 = models.CharField(
        max_length = 100,
    )
    City = models.CharField(
        max_length = 30,
        choices = (
            ('Ahmedabad' , 'Ahmedabad'),
            ('Surat' , 'Surat'),
            ('New Delhi' , 'New Delhi'),
            ('Noida' , 'Noida'),
            ('Jammu' , 'Jammu'),
            ('Kashmir' , 'Kashmir')
        )
    )

    def __str__(self):
        return self.username

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['First_Name','Last_Name','email','Phone_Number','Gender','Address_Line1','Address_Line2','City']

    objects = UserManager()
