from django.contrib import admin

from .models import Project, Tech


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ("techs",)
    list_display = ("title", "is_published", "created_at")
    list_filter = ("is_published", "techs")
    search_fields = ("title", "description")


@admin.register(Tech)
class TechAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
