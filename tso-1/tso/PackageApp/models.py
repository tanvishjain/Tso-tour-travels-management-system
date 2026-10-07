from django.db import models
from django.db.models.signals import pre_save 
from django.dispatch import receiver
from LocationApp.models import State, City
from datetime import datetime
from EmployeeApp.models import Guide, Driver
from Account.models import CustomUser

class Package(models.Model):
    Package_Name = models.CharField(
        max_length=100,
    )
    Price = models.IntegerField()
    Posture = models.ImageField(
        upload_to='tso/PackageImages',
    )
    Starting_Date = models.DateField()
    Ending_Date = models.DateField()
    Duration = models.CharField(
        max_length = 20, 
    )
    Available_Seats = models.IntegerField()
    Description = models.TextField()
    Registration_Deadline = models.DateTimeField()
    Tour_Status = models.CharField(
        max_length = 20,
        choices = (
            ('Scheduled' , 'Scheduled'),
            ('Ongoing' , 'Ongoing'),
            ('Completed' , 'Completed'),
        ),
        default = 'Scheduled',
    )
    Inclusions = models.TextField()
    Exclusions = models.TextField()
    Offer = models.CharField(
        choices = (
            ('Y' , 'Yes'),
            ('N' , 'No')
        ),
        max_length = 1
    )
    Discount_Percentage = models.IntegerField(
        default = 0
    )
    State = models.ForeignKey(
        State,
        on_delete = models.CASCADE
    )
    Guide = models.ForeignKey(
        Guide,
        on_delete = models.CASCADE
    )

    def duration(self):
        self.Duration = (self.Ending_Date - self.Starting_Date).days
    
    def is_available(self):
        if datetime.now().date > (self.Ending_Date).date:
            self.Tour_Status = 'Completed'
        elif datetime.now().date  > (self.Registration_Deadline).date and datetime.now().date  <= (self.Ending_Date).date:
            self.Tour_Status = 'Ongoing'
        else:
            self.Tour_Status = 'Scheduled'
    
    def __str__(self):
        return self.Package_Name
   
class Hotel(models.Model):
    Hotel_Name = models.CharField(
        max_length = 100,
    )
    Address_Line1 = models.CharField(
        max_length = 100,
    )
    Address_Line2 = models.CharField(
        max_length = 100,
    )
    City = models.ForeignKey(
        City,
        on_delete = models.CASCADE,
    )
    Zip_Code = models.IntegerField()
    Phone_No = models.CharField(
        max_length = 10,
    )
    Emergency_Phone = models.CharField(
        max_length = 10,
    )
    Email = models.EmailField()
    Price_Per_Night = models.DecimalField(
        max_digits = 10,
        decimal_places=2, 
    )
    Hotel_Classification = models.IntegerField()

    def __str__(self):
        return self.Hotel_Name

class Gallery(models.Model):
    Title = models.CharField(
        max_length = 50,
    )
    Image = models.ImageField(
        upload_to = 'Gallery_images/',
        null = True
    )
    Date_added = models.DateTimeField(
        default = datetime.now(),
    )
    Package = models.ForeignKey(
        Package,
        on_delete = models.CASCADE
    )  
    # User = models.ForeignKey(
    #     CustomUser,
    #     on_delete = models.CASCADE
    # )
    Username = models.CharField(
        max_length = 50,
        # default = 'honey'
    )
    
class Booking(models.Model):
    Booking_DateTime = models.DateTimeField()
    Total_Person = models.IntegerField()
    No_Of_Adults = models.IntegerField()
    No_Of_Children = models.IntegerField()
    Total_Amount = models.IntegerField()
    Payment_Mode = models.CharField(
        choices = (
            ('UPI' , 'UPI'),
            ('Net Banking' , 'Net Banking'),
            ('Debit/Credit Card' , 'Debit/Credit Card')
        ),
        max_length = 20,
    )
    User = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,
        default = 1,
    )
    Package = models.ForeignKey(
        Package,
        on_delete = models.CASCADE,
    )

    def save(self, *args, **kwargs):
        if not self.Booking_DateTime:
            self.Booking_DateTime = datetime.now()

        if not self.Package:
            self.Package = self.Package.id

        if not self.Total_Amount:
            if self.Package.Offer == 'Y':
                Price = self.Package.Price - (int(self.Package.Price*self.Package.Discount_Percentage)/100)
                self.Total_Amount = Price * self.Total_Person
                # self.Total_Amount = self.Package.Price * self.Total_Person
            else:
                self.Total_Amount = self.Package.Price * self.Total_Person
        super().save(*args, **kwargs)
            
    def __str__(self):
        return self.Package.Package_Name

class Cancellation(models.Model):
    Cancellation_DateTime = models.DateTimeField(
        default = datetime.now()
    )
    Reason = models.TextField()
    Cancellation_Fee = models.IntegerField(
        default = 0
    )
    Refund_Amount = models.IntegerField(
        default = 0
    )
    Booking = models.ForeignKey(
        Booking,
        on_delete = models.CASCADE
    )

    def cancellation_fees(self):
        if self.Cancellation_DateTime:
            days_before_tour_start = (self.Booking.Package.Starting_Date - self.Cancellation_DateTime).days 

            if days_before_tour_start >= 30:
                self.cancellation_fees = 0.00
            elif 7 <= days_before_tour_start < 30:
                self.cancellation_fees = self.Booking.Total_Amount * 0.25
            elif 1 <= days_before_tour_start < 7:
                self.cancellation_fees = self.Booking.Total_Amount * 0.50
            else:
                self.cancellation_fees = self.Booking.Total_Amount

        self.Refund_Amount = self.Booking.Total_Amount - self.cancellation_fees

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

class Vehicle(models.Model):
    Vehicle_Type = models.CharField(
        max_length = 20,
    )
    Registration_Number = models.CharField(
        max_length = 20,
    ) 
    Brand = models.CharField(
        max_length = 100,
    )
    Capacity = models.IntegerField()
    Fuel_Type = models.CharField(
        max_length = 10,
    )
    Insurance_Number = models.CharField(
        max_length = 20,
    )
    Vehicle_Category = models.CharField(
        max_length = 20,
    )
    Rental_Rate = models.DecimalField(
        max_digits = 10,
        decimal_places=2, 
    )
    Driver = models.ForeignKey(
        Driver,
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.Registration_Number
    
class Flight(models.Model):
    Airline_Name = models.CharField(
        max_length = 30,
        null = False
    )
    Flight_Number = models.CharField(
        max_length = 10,
        null = False
    )
    Available_Seats = models.IntegerField(
        null = False
    )
    
    def __str__(self):
        return self.Flight_Number
   
class Rail(models.Model):
    Train_Name = models.CharField(
        max_length = 100,
        null = False
    )
    Available_Seats = models.IntegerField(
        null = False
    )

    def __str__(self):
        return self.Train_Name

class Day_Description(models.Model):
    Day_Number = models.IntegerField()
    Description = models.TextField()
    Package = models.ForeignKey(
        Package,
        on_delete = models.CASCADE
    )
    Hotel = models.ForeignKey(
        Hotel,
        on_delete = models.CASCADE
    )
    Vehicle = models.ForeignKey(
        Vehicle,
        on_delete = models.SET_DEFAULT,
        default = None
    )
    Rail = models.ForeignKey(
        Rail,
        on_delete = models.SET_DEFAULT,
        default = None
    )
    Flight = models.ForeignKey(
        Flight,
        on_delete = models.SET_DEFAULT,
        default = None
    )
    City = models.ForeignKey(
        City,
        on_delete = models.CASCADE
    )

# class Custom(models.Model):
#     Custom = models.AutoField(
#         primary_key = True,
#         auto_created = True,
#     )
#     Custom_Name = models.CharField(
#         max_length = 50,
#         null = False,
#     )
#     Starting_Date = models.DateTimeField(
#         null = False,
#     )
#     Ending_Date = models.DateTimeField(
#         null = False,
#     )
#     Duration = models.CharField(
#         max_length = 20, 
#         null = False
#     )
#     Destination = models.TextField(
#         max_length = 500,
#         null = False,
#     )
#     Description = models.TextField(
#         max_length = 1000,
#         null = False,
#     )
#     Tour_Status = models.CharField(
#         max_length = 20,
#         choices = TOUR_STATUS_CHOICES,
#         default = 'Scheduled',
#         null = True
#     )
#     Created_At = models.DateTimeField(
#         default=datetime.now(),
#         null = False
#     )
#     Updated_At = models.DateTimeField(
#         default=datetime.now(),
#         null = False
#     )
#     Price = models.DecimalField(
#         max_digits = 10,
#         decimal_places=2, 
#         null = True
#     )
#     Hotel = models.ForeignKey(
#         Hotel,
#         on_delete = models.SET_NULL,
#         null = True
#     )
#     Vehicle = models.ForeignKey(
#         Vehicle,
#         on_delete = models.SET_NULL,
#         null = True
#     )
#     Rail = models.ForeignKey(
#         Rail,
#         on_delete = models.SET_NULL,
#         null = True
#     )
#     Flight = models.ForeignKey(
#         Flight,
#         on_delete = models.SET_NULL,
#         null = True
#     )
#     Guide = models.ForeignKey(
#         Guide,
#         on_delete = models.SET_NULL,
#         null = True
#     )
#     User = models.ForeignKey(
#         User_M,
#         on_delete = models.SET_NULL,
#         null = True
#     )

#     def __str__(self):
#         return self.Custom_Name

# # Create your models here.
# class Package(models.Model):
#     Package = models.AutoField(
#         primary_key = True,
#         auto_created= True,
#     )
#     Package_Name = models.CharField(
#         max_length=100, 
#         null = False
#     )
#     Price = models.DecimalField(
#         max_digits = 10,
#         decimal_places=2, 
#         null = False
#     )
#     Image = models.ImageField(
#         upload_to='adminimages',
#         default=""
#     )
#     Starting_Date = models.DateField(
#         null = False
#     )
#     Ending_Date = models.DateField( 
#         null = False
#     )
#     Duration = models.CharField(
#         max_length = 20, 
#         null = False
#     )
#     Available_Seats = models.IntegerField( 
#         null = False
#     )
#     Description = models.TextField(
#         null = False
#     )
#     Registration_Deadline = models.DateTimeField(
#         default=datetime.now(),
#         null = False
#     )
#     Tour_Status = models.CharField(
#         max_length = 20,
#         choices = TOUR_STATUS_CHOICES,
#         default = 'Scheduled',
#         null = False
#     )
#     Created_At = models.DateTimeField(
#         default=datetime.now(),
#         null = False
#     )
#     Updated_At = models.DateTimeField(
#         default=datetime.now(),
#         null = False
#     )
#     Inclusions = models.TextField(
#         null = False
#     )
#     Exclusions = models.TextField(
#         null = False
#     )
#     State = models.ForeignKey(
#         State,
#         on_delete = models.SET_NULL,
#         null = True
#     )
#     Guide = models.ForeignKey(
#         Guide,
#         on_delete = models.SET_NULL,
#         null = True
#     )
    
#     def __str__(self):
#         return self.Package_Name
   
# class Day_Description(models.Model):
#     Day = models.AutoField(
#         primary_key = True,
#         auto_created= True,
#         default=1
#     )
#     Day_Number = models.IntegerField(
#         null = False
#     )
#     Description = models.TextField(
#         null = False
#     )
#     Package = models.ForeignKey(
#         Package,
#         on_delete = models.SET_NULL,
#         null = True
#     )
#     Hotel = models.ForeignKey(
#         Hotel,
#         on_delete = models.SET_NULL,
#         null = True
#     )
#     Vehicle = models.ForeignKey(
#         Vehicle,
#         on_delete = models.SET_NULL,
#         null = True
#     )
#     Rail = models.ForeignKey(
#         Rail,
#         on_delete = models.SET_NULL,
#         null = True
#     )
#     Flight = models.ForeignKey(
#         Flight,
#         on_delete = models.SET_NULL,
#         null = True
#     )
#     City = models.ForeignKey(
#         City,
#         on_delete = models.SET_NULL,
#         null = True
#     )


# class Gallery(models.Model):
#     Gallery = models.AutoField(
#         primary_key = True,
#         auto_created = True,
        
#     )
#     Title = models.CharField(
#         max_length = 50,
#         null = False,
#         default = '',
#     )
#     Image = models.ImageField(
#         upload_to = 'Gallery_images/',
#         null = True
#     )
#     Description = models.TextField(
#         null = False,
#         default = ""
#     )
#     Date_added = models.DateTimeField(
#         default = datetime.now(),
#         null = False
#     )
#     Package = models.ForeignKey(
#         Package,
#         on_delete = models.SET_NULL,
#         null = True
#     )

#     def __str__(self):
#         return self.Title
    

# class Custom(models.Model):
#     Custom = models.AutoField(
#         primary_key = True,
#         auto_created = True,
#     )
#     Custom_Name = models.CharField(
#         max_length = 50,
#         null = False,
#     )
#     Starting_Date = models.DateTimeField(
#         null = False,
#     )
#     Ending_Date = models.DateTimeField(
#         null = False,
#     )
#     Duration = models.CharField(
#         max_length = 20, 
#         null = False
#     )
#     Destination = models.TextField(
#         max_length = 500,
#         null = False,
#     )
#     Description = models.TextField(
#         max_length = 1000,
#         null = False,
#     )
#     Tour_Status = models.CharField(
#         max_length = 20,
#         choices = TOUR_STATUS_CHOICES,
#         default = 'Scheduled',
#         null = True
#     )
#     Created_At = models.DateTimeField(
#         default=datetime.now(),
#         null = False
#     )
#     Updated_At = models.DateTimeField(
#         default=datetime.now(),
#         null = False
#     )
#     Price = models.DecimalField(
#         max_digits = 10,
#         decimal_places=2, 
#         null = True
#     )
#     Hotel = models.ForeignKey(
#         Hotel,
#         on_delete = models.SET_NULL,
#         null = True
#     )
#     Vehicle = models.ForeignKey(
#         Vehicle,
#         on_delete = models.SET_NULL,
#         null = True
#     )
#     Rail = models.ForeignKey(
#         Rail,
#         on_delete = models.SET_NULL,
#         null = True
#     )
#     Flight = models.ForeignKey(
#         Flight,
#         on_delete = models.SET_NULL,
#         null = True
#     )
#     Guide = models.ForeignKey(
#         Guide,
#         on_delete = models.SET_NULL,
#         null = True
#     )
#     User = models.ForeignKey(
#         User_M,
#         on_delete = models.SET_NULL,
#         null = True
#     )

#     def __str__(self):
#         return self.Custom_Name
    
# class Booking(models.Model):
#     Booking = models.AutoField(
#         primary_key = True,
#         auto_created = True,
#     )
#     Booking_DateTime = models.DateTimeField(
#         default=datetime.now(),
#         null = False
#     )
#     Total_Person = models.CharField(
#         max_length = 3,
#         null = False
#     )
#     No_Of_Adults = models.CharField(
#         max_length = 3,
#         null = False
#     )
#     No_Of_Children = models.CharField(
#         max_length = 3,
#         null = False
#     )
#     Name_Of_All = models.TextField(
#         max_length = 1000,
#         null = False,
#     )
#     Total_Amount = models.DecimalField(
#         max_digits = 10,
#         decimal_places=2, 
#         null = True
#     )
#     Payment_Status = models.CharField(
#         max_length = 20,
#         choices = PAYMENT_STATUS_CHOICES,
#         default = 'Paid',
#         null = True
#     )
#     Booking_Status = models.CharField(
#         max_length = 20,
#         choices = BOOKING_STATUS_CHOICES,
#         default = 'Confirmed',
#         null = True
#     )
#     User = models.ForeignKey(
#         User_M,
#         on_delete = models.SET_NULL,
#         null = True
#     )
#     Package = models.ForeignKey(
#         Package,
#         on_delete = models.SET_NULL,
#         null = True
#     )
#     Custom = models.ForeignKey(
#         Custom,
#         on_delete = models.SET_NULL,
#         null = True
#     )
#    # Payment = models.ForeignKey(
#    #     Payment,
#    #     on_delete = models.SET_NULL,
#    #     null = True
#    # )

# # Create your models here.
