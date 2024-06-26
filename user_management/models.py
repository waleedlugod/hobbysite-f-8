from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE, related_name="profile"
    )
    username = models.CharField(max_length=63, verbose_name="Display name")
    email = models.EmailField(default="example@example.com")

    def __str__(self):
        return str(self.username)
