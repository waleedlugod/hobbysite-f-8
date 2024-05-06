from django.db import models
from django.urls import reverse

from user_management.models import Profile


class Commission(models.Model):
    OPEN = "0"
    FULL = "1"
    COMPLETED = "2"
    DISCONTINUED = "3"
    STATUSES = {
        OPEN: "Open",
        FULL: "Full",
        COMPLETED: "Completed",
        DISCONTINUED: "Discontinued",
    }
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255, default=STATUSES[OPEN], choices=STATUSES)
    manpower_required = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("commissions:commission_detail", args=[str(self.pk)])


class Job(models.Model):
    OPEN = "0"
    FULL = "1"
    STATUSES = {
        OPEN: "Open",
        FULL: "Full",
    }
    commission = models.ForeignKey(
        to=Commission, on_delete=models.CASCADE, related_name="job"
    )
    role = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default=STATUSES[OPEN], choices=STATUSES)
    manpower_required = models.IntegerField()

    class Meta:
        ordering = ["status", "-manpower_required", "role"]

    def __str__(self):
        return str(self.role)


class JobApplication(models.Model):
    PENDING = "0"
    ACCEPTED = "1"
    REJECTED = "2"
    STATUSES = {
        PENDING: "Pending",
        ACCEPTED: "Accepted",
        REJECTED: "Rejected",
    }
    job = models.ForeignKey(
        to=Job, on_delete=models.CASCADE, related_name="job_application"
    )
    applicant = models.ForeignKey(
        to=Profile, on_delete=models.CASCADE, related_name="job_application"
    )
    status = models.CharField(
        max_length=255, default=STATUSES[PENDING], choices=STATUSES
    )
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["status", "-applied_on"]
