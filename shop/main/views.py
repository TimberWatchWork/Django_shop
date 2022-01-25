from django.shortcuts import render
from .models import Product

def index(request):
    Products = Product.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'Products': Products})


def cart(request):
    return render(request, 'main/cart.html')
