from ast import Return
from django.shortcuts import render
from django.http import HttpResponse
from .productForms import createProductForm


# Create your views here.
def createProduct(request):
    myForm = createProductForm()
    return render(request, 'create_product.html', {'form':myForm})

# store the created product


def storeProduct(request):
    if request.method == 'POST':
        datas = request.POST
        # create the createProductForm form and populate it with data
        form = createProductForm( request.POST )
        error = form.is_valid()
        return HttpResponse('The form submitted just fine')