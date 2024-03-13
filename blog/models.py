from django.db import models
from django.forms import DateField

# Models: ProductType, Product


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ["name"]


class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        "ArticleCategoty", on_delete=models.SET_NULL, related_name="articles", default=1
    )
    entry = models.TextField()
    created_on = models.DateTimeField(DateField.auto_now_add)
    updated_on = models.DateTimeField(DateField.auto_now)

    class Meta:
        ordering = ["-created_on"]


# Create your models here.
