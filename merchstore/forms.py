from django import forms

from .models import Product, Transaction


class ProductForm(forms.Form):
    class Meta:
        model = Product
        fields = "__all__"


class TransactionForm(forms.Form):
    class Meta:
        model = Transaction
        fields = "__all__"