from django.shortcuts import render
from .models import Product


def cookie_city(request):
    city = '!'
    if request.method == 'GET':
        if 'city' in request.COOKIES:
            city = request.COOKIES['city']
    elif request.method == 'POST':
        city = request.POST.get('city')

    return city


def index(request):
    city = cookie_city(request)
    products = Product.objects.all()
    response = render(request, 'main/index.html', {'title': 'Главная страница сайта', 'products': products,
                                                   'city': city,})
    response.set_cookie('city', city)
    return response


def cart(request):
    city = cookie_city(request)
    response = render(request, 'main/cart.html', {'city': city, })
    response.set_cookie('city', city)
    return response

