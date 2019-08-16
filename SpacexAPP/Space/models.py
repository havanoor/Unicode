from django.db import models

# Create your models here.

class spaceClass(models.Model):
    flight_number=models.IntegerField(primary_key=True)
    mission_name=models.CharField(max_length=100)
    rocket_name=models.CharField(max_length=100)
    mission_patch=models.CharField(max_length=100,null=True)
    time=models.DateTimeField(null=True)
    
