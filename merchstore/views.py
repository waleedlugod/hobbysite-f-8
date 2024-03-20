from django.shortcuts import render

from .models import Product, ProductType

def merch_list_view(request):
    types = ProductType.objects.all()
    ctx = {'types': types}

    return render(request, 'merchstore/product_list.html', ctx)

def merch_detail_view(request, pk):
    product = Product.objects.get(pk=pk)
    ctx = {'product': product}

    return render(request, 'merchstore/product_detail.html', ctx)
