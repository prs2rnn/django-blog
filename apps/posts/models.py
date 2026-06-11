import math

from django.db import models
from django.urls import reverse

from .markdown import render_markdown


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, verbose_name="URL")
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})

    @property
    def words_count(self):
        return len(self.content.split())

    @property
    def reading_time(self):
        return math.ceil(self.words_count / 200)

    @property
    def was_updated(self):
        return (self.updated_at - self.created_at).total_seconds() > 60

    @property
    def html(self):
        return render_markdown(self.content)
