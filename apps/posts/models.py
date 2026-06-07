import math

import markdown
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, verbose_name="URL")
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]

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
        return markdown.markdown(
            self.content,
            extensions=[
                "fenced_code",
                "tables",
                "toc",
            ],
        )
