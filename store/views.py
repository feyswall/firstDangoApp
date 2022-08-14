from ast import Return
from django.shortcuts import render
from django.http import HttpResponse
from .productForms import createProductForm
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .productSerializer import productSerializerFunction
from . import models


# Create your views here.
def createProduct(request):
    myForm = createProductForm()
    return render(request, 'create_product.html', {'form': myForm})


# store the created product


def storeProduct(request):
    if request.method == 'POST':
        datas = request.POST
        # create the createProductForm form and populate it with data
        form = createProductForm(request.POST)
        error = form.is_valid()
        return HttpResponse('The form submitted just fine')


@api_view()
def showProducts(request):
    productsqueryset = models.Product.objects.select_related('collection').all()
    productJson = productSerializerFunction(productsqueryset, many=True)
    return Response(productJson.data)
