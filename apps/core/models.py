from django.db import models


class SiteStats(models.Model):
    visits = models.PositiveIntegerField(default=0)

    @classmethod
    def get(cls):
        return cls.objects.get_or_create(pk=1)[0]

    def __str__(self):
        return f"Visits: {self.visits}"
