from django.db.models.signals import post_init
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

receiver(post_init, sender=Profile)


def create_profile(sender, instance, **kwargs):
    profile = Profile.objects.create(display_name=instance.username)
