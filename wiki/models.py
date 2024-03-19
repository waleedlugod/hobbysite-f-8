from django.db import models
from django.urls import reverse


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wiki_detail", kwargs={"pk": self.pk})

    ## reverse("wiki:wiki_detail")

    class Meta:
        ordering = ["name"]


class Article(models.Model):
    title = models.CharField(max_length=255)
    entry = models.TextField()
    category = models.ForeignKey(
        ArticleCategory, on_delete=models.CASCADE, related_name="artcles"
    )

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("wiki_detail", kwargs={"pk": self.pk})


# Create your models here.
