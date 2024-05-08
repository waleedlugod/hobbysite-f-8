from django import forms

from .models import Product, Transaction


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "type", "description", "price", "stock", "status"]


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["amount"]
