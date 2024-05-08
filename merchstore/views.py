from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Product, ProductType, Transaction
from .forms import ProductForm, TransactionForm


def product_list(request):
    user_products = []
    # all_products = []
    # if request.user.is_authenticated():
    user = request.user
    user_products = Product.objects.filter(owner__username=request.user.profile.username)
    all_products = Product.objects.exclude(owner__username=request.user.profile.username)
    # else:
        # user = "You are not logged in."
        # all_products = Product.objects.all()
    
    ctx = {
        "user" : user, 
        'user_products': user_products, 
        "all_products": all_products
    }
    return render(request, "merchstore/product_list.html", ctx)

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    seller = product.owner
    transaction_form = TransactionForm()
    if request.method == "POST":
        transaction_form = TransactionForm(request.POST, product=product)
        if transaction_form.is_valid():
            transaction = Transaction()
            transaction.product = product
            transaction.amount = transaction_form.cleaned_data.get("amount")
            transaction.status = "ON_CART"
            if request.user.is_authenticated:
                transaction.buyer = request.user
                if product.stock == 0:
                    product.status = "OUT_OF_STOCK"
                else:
                    product.status = "AVAILABLE"
                    product.save(update_fields=["stock", "status"])
                    transaction.save()
                    return redirect("merchstore:cart")
            else:
                return redirect("login")


@login_required
def product_create(request):
    user = request.user
    product_form = ProductForm()
    if request.method == "POST":
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product = product_form.save()
            product.owner = user
            if product.stock == 0:
                product.status = "OUT_OF_STOCK"
            product.save()
            return redirect("merchstore:product_detail", pk=product.pk)
    
    ctx = {
        "form" : product_form,
        "user" : user
    }
    return render(request, "merchstore/product_create.html", ctx)


@login_required
def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    user = request.user
    product_form = ProductForm()
    if request.method == "POST":
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product.owner = user
            if product.stock == 0:
                product.status = "OUT_OF_STOCK"
            product.save()
            return redirect("merchstore:product_detail", pk=product.pk)
        
    ctx = {
        "form" : product_form, 
        "user" : user
    }
    return render(request, "merchstore/product_update.html", ctx)            


@login_required
def cart_list(request):
    user = request.user
    products = Transaction.objects.filter(buyer=user).order_by("owner")
    ctx = {
        "user" : user,
        "products": products
    }
    return render(request, "merchstore/cart.html", ctx)


@login_required
def transaction_list(request):
    user = request.user
    transactions = Transaction.objects.filter(product__owner=user).order_by("buyer")
    ctx = {
        "user" : user,
        "transactions": transactions
    }
    return render(request, "merchstore/transactions.html", ctx)