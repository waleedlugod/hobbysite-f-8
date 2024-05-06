from django.db import models
from django.urls import reverse

from user_management.models import Profile


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Article Categories"


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile,
        null=True,
        on_delete=models.SET_NULL,
        related_name="articles",
    )
    category = models.ForeignKey(
        "ArticleCategory",
        null=True,
        on_delete=models.SET_NULL,
        related_name="articles",
    )
    entry = models.TextField()
    header_image = models.ImageField(
        upload_to="images/", null=False, default="default.jpg"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("blog:blog-detail", args=[self.pk])

    class Meta:
        ordering = ["-created_on"]


class Comment(models.Model):
    author = models.ForeignKey(
        Profile, null=True, on_delete=models.SET_NULL, related_name="comments"
    )
    article = models.ForeignKey(
        "Article", on_delete=models.CASCADE, related_name="comments"
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]


class ArticleImage(models.Model):
    article = models.ForeignKey(
        "Article", on_delete=models.CASCADE, related_name="images"
    )
    image = models.FileField(upload_to="images/", null=False)
