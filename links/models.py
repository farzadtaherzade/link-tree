from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Link(models.Model):
    LAYOUT_TYPE_CHOICES = (
        ("classic", "Classic"),
        ("features", "Features"),
    )

    title = models.CharField(max_length=155)
    url = models.URLField()
    thumbnail = models.ImageField(
        validators=[FileExtensionValidator(["png", "jpg"])], null=True, blank=True)
    is_active = models.BooleanField(null=False, blank=True, default=True)

    layout_type = models.CharField(
        choices=LAYOUT_TYPE_CHOICES, default="classic")

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="links")

    def __str__(self):
        return f"url: {self.url} belongs to {self.user.username}"

    class Meta:
        pass


class Lock(models.Model):
    pass
