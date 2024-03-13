from django.urls import reverse
from django.db import models
from django.forms import DateField

# Models: ProductType, Product


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        "ArticleCategory",
        null=True,
        on_delete=models.SET_NULL,
        related_name="articles",
        default=1,
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:blog-detail", args=[self.pk])

    class Meta:
        ordering = ["-created_on"]


# Create your models here.
