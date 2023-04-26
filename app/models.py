from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')
    etsy_link = models.CharField(max_length=1000, default="https://www.etsy.com/shop/FitzPrintsgb")
    source_link = models.CharField(max_length=1000, blank=True)
    description = models.TextField()
    print_time = models.FloatField()
    filament_used = models.FloatField()
    filament_cost = models.FloatField()
    profit = models.FloatField()

    def __str__(self):
        return self.name
    