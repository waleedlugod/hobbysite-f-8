from django.db import models
from django.urls import reverse


class Commission(models.Model):
    STATUS_CHOICES = {
        "O": "Open",
        "F": "Full",
        "C": "Completed",
        "DC": "Discontinued",
    }
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255, default=STATUS_CHOICES["O"], choices=STATUS_CHOICES)
    people_required = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("commissions:commission_detail", args=[str(self.pk)])


class Job(models.Model):
    STATUS_CHOICES = {
        "O": "Open",
        "F": "Full",
    }
    commission = models.ForeignKey(
        to=Commission, on_delete=models.CASCADE, related_name="Job"
    )
    role = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default=STATUS_CHOICES["O"], choices=STATUS_CHOICES)
    people_required = models.IntegerField()

    class Meta:
        ordering = ["-status", "-people_required", "role"]
