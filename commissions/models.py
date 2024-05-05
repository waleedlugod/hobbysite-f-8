from django.db import models
from django.urls import reverse

from user_management.models import Profile


class Commission(models.Model):
    STATUS_CHOICES = {
        "O": "Open",
        "F": "Full",
        "C": "Completed",
        "DC": "Discontinued",
    }
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=255, default=STATUS_CHOICES["O"], choices=STATUS_CHOICES
    )
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
        to=Commission, on_delete=models.CASCADE, related_name="job"
    )
    role = models.CharField(max_length=255)
    status = models.CharField(
        max_length=255, default=STATUS_CHOICES["O"], choices=STATUS_CHOICES
    )
    people_required = models.IntegerField()

    class Meta:
        # TODO: make ordering better
        ordering = ["-status", "-people_required", "role"]


class JobApplication(models.Model):
    STATUS_CHOICES = {
        "P": "Pending",
        "A": "Accepted",
        "R": "Rejected",
    }
    job = models.ForeignKey(
        to=Job, on_delete=models.CASCADE, related_name="job_application"
    )
    applicant = models.ForeignKey(
        to=Profile, on_delete=models.CASCADE, related_name="job_application"
    )
    status = models.CharField(
        max_length=255, default=STATUS_CHOICES["P"], choices=STATUS_CHOICES
    )
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # TODO: fix ordering
        ordering = ["-applied_on"]
