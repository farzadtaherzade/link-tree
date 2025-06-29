from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Profile(models.Model):
    avatar = models.ImageField(upload_to="uploads/", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    display_name = models.CharField()

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return f"{self.user.username}"


class Socials(models.Model):
    github = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)

    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name='socials')

    def __str__(self):
        return f"{self.profile.user.username}'s social links"
