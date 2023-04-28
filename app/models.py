from django.db import models
from PIL import Image

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
    profit = models.FloatField(blank=True)
    colour = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
    
    def average_color(self, image_path, border_percent=12):
        image = Image.open(image_path).convert('RGB')
        width, height = image.size

        # Calculate the border size to exclude
        border_width = int(width * border_percent / 100)
        border_height = int(height * border_percent / 100)

        # Crop the image to exclude the border
        cropped_image = image.crop((border_width, border_height, width - border_width, height - border_height))

        # Get pixel data
        pixels = cropped_image.getdata()

        # Calculate the average color
        r_total, g_total, b_total = 0, 0, 0
        num_pixels = cropped_image.width * cropped_image.height
        for r, g, b in pixels:
            r_total += r
            g_total += g
            b_total += b

        avg_r = int(r_total / num_pixels)
        avg_g = int(g_total / num_pixels)
        avg_b = int(b_total / num_pixels)

        return (avg_r, avg_g, avg_b)
    
    def save(self, *args, **kwargs):
        self.profit = self.price - self.filament_cost
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        image.thumbnail((1000, 1000))
        image.save(self.image.path)
        self.colour = self.average_color(self.image.path)
        super().save(update_fields=['colour'])