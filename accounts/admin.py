from django.contrib import admin
from .models import Profile, Socials


class SocialInline(admin.StackedInline):  # Changed to StackedInline
    model = Socials
    extra = 1


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    inlines = [SocialInline]
