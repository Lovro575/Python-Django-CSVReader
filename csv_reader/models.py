from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
   
class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    truck_number = models.IntegerField(unique=True)

class Meta:
    #making sure that each vehicle is associated with only one user
    unique_together = ('user', 'truck_number')