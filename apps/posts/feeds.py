from django.contrib.syndication.views import Feed
from django.urls import reverse

from .models import Post


class LatestPostsFeed(Feed):
    title = "Andrey Perestoronin RSS Feed"
    description = "My latest posts"
    link = "/posts/"

    def items(self):
        return Post.objects.filter(is_published=True)[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:200]

    def item_link(self, item):
        return reverse("posts:detail", args=[item.slug])

    def item_pubdate(self, item):
        return item.created_at

    def item_updateddate(self, item):
        return item.updated_at
