from django.db import models

# Create your models here.
class Vehicle(models.Model):
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    
    def vehicle_info(self):
        return f'({self.brand} costs {self.price})'
        # Toyota costs 500000
    
    def ___str__(self):
        return Vehicle.brand

class Car(Vehicle):
    doors = models.IntegerField()
    
    def vehicle_info(self):
        return f'({self.brand} Car with {self.doors} doors costs {self.price})'
        # Toyota Car with 4 doors costs 500000
    
    def __str__(Vehicle):
        return Vehicle.brand

class Motorcycle(Vehicle):
    helmet_included = models.BooleanField()
    
    def vehicle_info(self):
        return f'({self.brand} Motorcycle costs {self.price})'
        # Honda Motorcycle costs 120000
    
    def __str__(Vehicle):
        return Vehicle.brand