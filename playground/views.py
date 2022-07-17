from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def say_hellow(request):
    return render(request, "index.html", {'name': 'mjeba'})
