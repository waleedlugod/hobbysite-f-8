from django.db import models
from django.urls import reverse


class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    people_required = models.IntegerField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()

    class Meta:
        ordering = ["-created_on"]

    def get_absolute_url(self):
        return reverse("commissions:commission_detail", args=[str(self.pk)])


class Comment(models.Model):
    commission = models.ForeignKey(
        to=Commission, on_delete=models.CASCADE, related_name="comments"
    )
    entry = models.TextField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()

    class Meta:
        ordering = ["-created_on"]
