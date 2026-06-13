from django.db import models


class SiteStats(models.Model):
    visits = models.PositiveIntegerField(default=0)

    @classmethod
    def get(cls):
        return cls.objects.get_or_create(pk=1)[0]

    def __str__(self):
        return f"Visits: {self.visits}"


class Tech(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    github_url = models.URLField(blank=True, null=True)
    demo_url = models.URLField(blank=True, null=True)

    techs = models.ManyToManyField(Tech)

    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField()

    STATUS_CHOICES = [
        ("wip", "Work in progress"),
        ("done", "Finished"),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
