from django.conf import settings
from django.http import HttpRequest


def site_info(request: HttpRequest):
    return {"site_commit": settings.SITE_COMMIT, "site_updated": settings.SITE_UPDATED}
