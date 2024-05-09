from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Product, Transaction
from .forms import ProductForm, TransactionForm
from django.contrib.auth.decorators import login_required


def product_list(request):
    user_products = []
    all_products = []
    if request.user.is_authenticated:
        user = request.user.profile
        user_products = Product.objects.filter(
            owner__username=request.user.profile.username)
        all_products = Product.objects.exclude(
            owner__username=request.user.profile.username)
    else:
        all_products = Product.objects.all()

    ctx = {
        'user_products': user_products,
        "all_products": all_products
    }
    return render(request, "merchstore/product_list.html", ctx)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    transaction_form = TransactionForm()
    if request.method == "POST":
        transaction_form = TransactionForm(request.POST, product=product)
        if transaction_form.is_valid():
            transaction = transaction_form.save(commit=False)
            transaction.product = product
            if product.stock == 0:
                product.status = Product.OUT_OF_STOCK
            product.save(update_fields=["stock", "status"])
            if request.user.is_authenticated:
                transaction.buyer = request.user.profile
            else:
                return redirect("login")
            transaction.save()
            return redirect("merchstore:cart")

    ctx = {
        "product": product,
        "form": transaction_form,
    }
    return render(request, "merchstore/product_detail.html", ctx)


@login_required
def product_create(request):
    user = request.user.profile
    product_form = ProductForm()
    if request.method == "POST":
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product = product_form.save()
            product.owner = user
            if product.stock == 0:
                product.status = Product.OUT_OF_STOCK
            product.save()
            return redirect("merchstore:detail", pk=product.pk)

    ctx = {
        "form": product_form,
        "user": user
    }
    return render(request, "merchstore/product_create.html", ctx)


@login_required
def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    user = request.user.profile
    if request.method == "POST":
        product_form = ProductForm(request.POST, instance=product)
        if product_form.is_valid():
            product.owner = user
            if product.stock == 0:
                product.status = Product.OUT_OF_STOCK
            product_form.save()
            return redirect("merchstore:detail", pk=product.pk)
    else:
        product_form = ProductForm(instance=product)

    ctx = {
        "form": product_form,
        "product": product,
        "user": user
    }
    return render(request, "merchstore/product_update.html", ctx)


@login_required
def cart_list(request):
    user = request.user.profile
    cart = Transaction.objects.filter(buyer=user).order_by("product__owner")
    ctx = {
        "user": user,
        "cart": cart
    }
    return render(request, "merchstore/cart.html", ctx)


@login_required
def transaction_list(request):
    user = request.user.profile
    transactions = Transaction.objects.filter(
        product__owner=user).order_by("buyer__user")
    ctx = {
        "user": user,
        "transactions": transactions
    }
    return render(request, "merchstore/transactions.html", ctx)
