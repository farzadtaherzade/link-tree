from django.contrib import admin
from .models import Link

# Register your models here.


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "url", "is_active", "user", "layout_type"]
    list_filter = ["is_active", "layout_type"]
    search_fields = ["title"]
