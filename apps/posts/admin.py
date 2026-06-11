from django.contrib import admin

from . import models


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)
