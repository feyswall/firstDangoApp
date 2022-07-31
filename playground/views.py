from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
# Create your views here.


@api_view()
def say_hellow(request, id):
    try:
        queryset = Product.objects.get(id=id)
        serializer = ProductSerializer(queryset)
        return  Response( serializer.data )
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def forMyStudent(request):
    return render(request, "about.html", {'prev':'there to back'})
