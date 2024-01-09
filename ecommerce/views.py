from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'pages/home/home.html', context={
        'name':'Ecommerce',
        })

def product(request, id):
    return render(request, 'pages/details/details.html', context={
        'name':'Ecommerce',
        })