from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    
    def product_info(self):
        # Example output: "Laptop costs 30000"
        return f'{self.name} costs {self.price}'

    def __str__(self):
        return self.name

