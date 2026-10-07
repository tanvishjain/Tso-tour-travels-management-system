from django.db import models
from datetime import datetime
from Account.models import CustomUser

# Create your models here.
class Contact(models.Model):
    First_Name = models.CharField(
        max_length = 50,
    )
    Last_Name = models.CharField(
        max_length = 50,
    )
    Email = models.EmailField()
    Phone_Number = models.CharField(
        max_length=10,
    )
    Message = models.TextField()

class Feedback(models.Model):
    Rating = models.CharField(
        choices = (
            ('1' , '1'),
            ('2' , '2'),
            ('3' , '3'),
            ('4' , '4'),
            ('5' , '5'),
        ),
        max_length = 1
    )
    Feedback = models.TextField()
    Date_Time = models.DateTimeField(
        default = datetime.now()
    )
    User = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,
        default = 1
    )