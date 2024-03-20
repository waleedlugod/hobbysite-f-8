from django.db import models
from django.urls import reverse

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return '{}' .format(self.name)
    
    class Meta:
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(
        ProductType,
        null = True,
        on_delete=models.SET_NULL,
        related_name= 'products'
    )
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=50)

    def __str__(self):
        return '{}' .format(self.name)
    
    def get_absolute_url(self):
        return reverse('merchstore:detail', args=[self.pk])
    
    class Meta:
        ordering = ['name']