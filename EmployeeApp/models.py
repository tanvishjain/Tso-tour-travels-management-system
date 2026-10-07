from django.db import models
from Account.models import CustomUser
from LocationApp.models import City
# from PackageApp import Package

# Create your models here.
class Guide(models.Model):
    First_Name = models.CharField(
        max_length = 50,
    )
    Middle_Name = models.CharField(
        max_length = 50,
    )
    Last_Name = models.CharField(
        max_length = 50,
    )
    Address_Line1 = models.CharField(
        max_length = 100,
    )
    Address_Line2 = models.CharField(
        max_length = 100,
    )
    City = models.ForeignKey(
        City,
        on_delete = models.CASCADE
    )
    Zip_Code = models.IntegerField()
    Phone_No = models.CharField(
        max_length = 10,
    )
    Emergency_Phone = models.CharField(
        max_length = 10,
    )
    Email = models.EmailField()
    Gender = models.CharField(
        max_length = 1,
        choices = (
            ('M' , 'Male'),
            ('F' , 'Female'),
            ('O' , 'Other')
        ),
    )

    def __str__(self):
        return self.First_Name + ' ' + self.Middle_Name + ' ' + self.Last_Name
   
class Driver(models.Model):
    First_Name = models.CharField(
        max_length = 50,
    )
    Middle_Name = models.CharField(
        max_length = 50,
    )
    Last_Name = models.CharField(
        max_length = 50,
    )
    Address_Line1 = models.CharField(
        max_length = 100,
    )
    Address_Line2 = models.CharField(
        max_length = 100,
    )
    City = models.ForeignKey(
        City,
        on_delete = models.CASCADE
    )
    Zip_Code = models.IntegerField()
    Phone_No = models.CharField(
        max_length = 10,
    )
    Emergency_Phone = models.CharField(
        max_length = 10,
    )
    Email = models.EmailField()
    License_Number = models.CharField(
        max_length = 20,
        null = False
    )
    Gender = models.CharField(
        max_length = 1,
        choices = (
            ('M' , 'Male'),
            ('F' , 'Female'),
            ('O' , 'Other')
        ),
    )

    def __str__(self):
        return self.First_Name + ' ' + self.Middle_Name + ' ' + self.Last_Name
  
class Employee(CustomUser):
    Salary = models.IntegerField()
    Designation = models.CharField(
        max_length = 50,
    )
    Active_Status = models.CharField(
        choices = (
            ('Y' , 'Yes'),
            ('N' , 'No')
        ),
        max_length = 1
    )

    def __str__(self):
        return self.First_Name + ' ' + self.Middle_Name + ' ' + self.Last_Name

class Salary(models.Model):
    Total_Amount = models.IntegerField()
    Net_Salary = models.IntegerField()
    Guide = models.ForeignKey(
        Guide,
        on_delete = models.SET_DEFAULT,
        default = 'None'
    )
    Driver = models.ForeignKey(
        Driver,
        on_delete = models.SET_DEFAULT,
        default = 'None'
    )
    Employee = models.ForeignKey(
        Employee,
        on_delete = models.SET_DEFAULT,
        default = 'None'
    )
    # Package = models.ForeignKey(
    #     Package,
    #     on_delete = models.SET_DEFAULT,
    #     default = 'None'
    # )
 