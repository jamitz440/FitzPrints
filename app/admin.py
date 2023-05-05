from django.contrib import admin
from .models import Product, Filament, File

# Register your models here.

admin.site.register(Product)
admin.site.register(Filament)
admin.site.register(File)
