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

    order = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"url: {self.url} belongs to {self.user.username}"

    def save(self, *args, **kwargs):
        if not self.id:
            max_order = Link.objects.aggregate(
                models.Max('order'))['order__max'] or 0
            self.order = max_order + 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['order']


class Lock(models.Model):
    pass
