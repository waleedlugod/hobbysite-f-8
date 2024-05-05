from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=63, verbose_name="Display name")
    email = models.EmailField(default="example@example.com")

    def __str__(self):
        return self.username
