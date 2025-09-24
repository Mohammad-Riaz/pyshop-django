from django.http import HttpResponse
from django.shortcuts import render
from .models import Product



def index(request):
    products = Product.objects.all().order_by('-id')
    return render(request, # the http request
                  'index.html', # name of our template
                  {'products': products}) # the data to be passed through the template


def new(request):
    return HttpResponse("NEW PRODUCTS: ")