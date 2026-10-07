from django.db import models

# Create your models here.
class State(models.Model):
    State_Name = models.CharField(
        max_length = 20,
        unique = True,
        null = False
    )

    def __str__(self):
        return self.State_Name
    

class City(models.Model):
    City_Name = models.CharField(
        max_length = 30,
        unique = True,
        null = False,
    )  
    State = models.ForeignKey(
        State,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.City_Name
