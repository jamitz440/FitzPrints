from django.shortcuts import render , redirect, get_object_or_404, reverse
from django.http import HttpResponse
from .models import Product, Filament
from .forms import UploadForm as Upload, UpdateForm as Update

from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def index(request):
    products = Product.objects.filter(user = request.user)
    context = { "products": products }
    return render(request, "app/index.html", context)


def dice(request):
    products = Product.objects.all()
    context = { "products": products }
    return render(request, "app/dice.html", context)


def upload(request):
    if request.method == 'POST':
        form = Upload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'app/index.html')
    else:
        form = Upload()
    return render(request, 'app/upload.html', {'form': form})

def filament(request):
    context = { "filaments": Filament.objects.all() }
    return render(request, "app/filaments.html", context)

def file_detail(request, name):

    product = Product.objects.get(name=name)
    if request.method == 'POST':
        form = Update(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('app:file_detail', name=product.name)
        else:
            # if form is not valid, render the same page with the errors
            context = { "product": product, "form": form}
            return render(request, "app/file_detail.html", context)
    else:
        form = Update(instance=product)

        context = { "product": product, "form": form}
        return render(request, "app/file_detail.html", context)

