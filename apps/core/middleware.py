from django.db.models import F
from django.http import HttpRequest

from .models import SiteStats


class SiteVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        if not request.session.get("site_visited"):
            SiteStats.objects.update(visits=F("visits") + 1)

            request.session["site_visited"] = True

        response = self.get_response(request)

        return response
