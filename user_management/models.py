from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.oneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=63)
