from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Profile(models.Model):
    avatar = models.ImageField(upload_to="uploads/", null=True, blank=False)
    bio = models.TextField(null=True, blank=True)
    display_name = models.CharField()

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return f"{self.user.username}"
