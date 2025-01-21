from .models import Product
import os
from django.conf import settings
from django.shortcuts import render


def home_page(request):
    return render(request, 'catalog/home.html')


def product_detail(request):
    products = Product.objects.all()
    return render(request, 'catalog/showcase.html', {'products': products})


def about(request):
    file = os.path.join(settings.BASE_DIR, 'media/text/about.txt')
    with open(file, 'r', encoding='UTF-8') as file:
        content = file.read()

    return render(request, 'catalog/about.html', {'content': content})
