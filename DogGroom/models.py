from django.db import models
from django.conf import settings
from .const import *


# Create your models here.

class Dog(models.Model):

    dogid = models.AutoField(primary_key = True)
    dogname = models.CharField(max_length = 50)#, default = 'default')
    dob = models.DateField(null = True)
    breed = models.CharField(max_length = 2, choices = breed_list.items(), null = True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    
    def __str__(self):
        return str.format('Name: {0},    DoB: {1},    Breed: {2}', 
            self.dogname, self.dob,  breed_list[self.breed])

class Appointment(models.Model):
    
    bookingid = models.AutoField(primary_key = True)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    dog = models.ForeignKey(Dog, on_delete = models.CASCADE)
    date = models.DateField(null=True)
    starttime = models.CharField(max_length = 5, null = True)
    washoption = models.CharField(max_length = 2, choices = wash_options.items(), default = 'WO')
    instruction = models.TextField(null = True, blank = True)

    class Meta:
        unique_together = (('client', 'dog', 'date', 'starttime'),)
    
    def __str__(self):
        showbooking = str.format('Puppy: {0}, Start Time: {1}, Option: {2}, Date: {3}, Client: {4}',  
                          self.dog, self.starttime, wash_options[self.washoption], self.date, self.client.first_name)
        return showbooking

