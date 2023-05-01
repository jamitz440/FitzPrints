from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import UploadForm as Upload
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

def file_detail(request, name):
    product = Product.objects.get(name=name)
    context = { "product": product }
    return render(request, "app/file_detail.html", context)

def upload(request):
    if request.method == 'POST':
        form = Upload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'app/index.html')
    else:
        form = Upload()
    return render(request, 'app/upload.html', {'form': form})

