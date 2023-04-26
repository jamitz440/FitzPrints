from django.shortcuts import render
from django.http import HttpResponse
from .models import Product



# Create your views here.
def index(request):
    products = Product.objects.all()
    context = { "products": products }
    return render(request, "app/index.html", context)


def dice(request):
    products = Product.objects.all()
    context = { "products": products }
    return render(request, "app/dice.html", context)

def file_detail(request, name):
    product = Product.objects.get(name=name)
    context = { "product": product }
    return render(request, "app/file_detail.html", context)