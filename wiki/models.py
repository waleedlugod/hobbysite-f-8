from django.db import models
from django.urls import reverse


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    ## reverse("wiki:wiki_detail")

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Article categories"


class Article(models.Model):
    title = models.CharField(max_length=255)
    entry = models.TextField()
    category = models.ForeignKey(
        ArticleCategory, on_delete=models.SET_NULL, null=True, related_name="articles"
    )

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("wiki:article-detail", args=[str(self.pk)])


# Create your models here.
