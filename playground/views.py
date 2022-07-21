from itertools import product
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
# Create your views here.


def say_hellow(request):
    return render(request, "index.html", {'name': 'mjeba'})
