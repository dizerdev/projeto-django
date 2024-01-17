from django.http import HttpResponse
from django.shortcuts import render
from utils.product.factory import make_product
# Create your views here.


def home(request):
    return render(request, 'pages/home/home.html', context={
        'name':'Ecommerce',
        'products': [make_product() for _ in range(10)],        
        })


def product(request, id):
    return render(request, 'pages/details/details.html', context={
        'name':'Ecommerce',
        'product': make_product(),
        'is_detail_page': True,
        })

