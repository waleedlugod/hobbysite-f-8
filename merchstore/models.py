from django.db import models
from django.urls import reverse

from user_management.models import Profile


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(
        ProductType, null=True, on_delete=models.SET_NULL, related_name="products"
    )
    owner = models.ForeignKey(
        Profile, null=True, on_delete=models.CASCADE, related_name="products_owned"
    )
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=50)
    stock = models.PositiveIntegerField(default=0)
    AVAILABLE = "AV"
    ON_SALE = "SA"
    OUT_OF_STOCK = "OOS"
    STATUS_CHOICES = [
        (AVAILABLE, "Available"),
        (ON_SALE, "On Sale"),
        (OUT_OF_STOCK, "Out of Stock"),
    ]
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=AVAILABLE)

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse("merchstore:detail", args=[str(self.pk)])

    def get_status(self):
        return self.status

    class Meta:
        ordering = ["name", "status"]


class Transaction(models.Model):
    buyer = models.ForeignKey(
        Profile, null=True, on_delete=models.SET_NULL, related_name="products_bought"
    )
    product = models.ForeignKey(
        Product, null=True, on_delete=models.SET_NULL, related_name="buyers"
    )
    amount = models.PositiveIntegerField()
    ON_CART = "OC"
    TO_PAY = "TP"
    TO_SHIP = "TS"
    TO_RECEIVE = "TR"
    DELIVERED = "D"
    STATUS_CHOICES = (
        (ON_CART, "On Cart"),
        (TO_PAY, "To Pay"),
        (TO_SHIP, "To Ship"),
        (TO_RECEIVE, "To Receive"),
        (DELIVERED, "Delivered")
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=ON_CART)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{ self.buyer } bought {self.amount} - {self.product} item/s'
    
    # def get_status(self):
    #     return self.status

    def save(self, *args, **kwargs):
        self.product.stock -= self.amount
        self.product.save()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["status"]
