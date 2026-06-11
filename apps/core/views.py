from django.views.generic import TemplateView

from apps.core.models import SiteStats

from ..posts.models import Post


class HomeView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Home".lower()
        context["recent_posts"] = Post.objects.filter(is_published=True).order_by(
            "-created_at"
        )[:5]

        posts = Post.objects.filter(is_published=True)

        context["post_count"] = posts.count()
        context["total_words"] = sum(post.words_count for post in posts)
        context["first_post"] = posts.order_by("created_at").first()
        context["visits"] = SiteStats.get().visits

        return context


class BasePageView(TemplateView):
    page_title = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.page_title.lower()
        return context


class AboutView(BasePageView):
    template_name = "core/about.html"
    page_title = "About"


class ContactView(BasePageView):
    template_name = "core/contact.html"
    page_title = "Contact"


class UsesView(BasePageView):
    template_name = "core/uses.html"
    page_title = "Uses"


class NowView(BasePageView):
    template_name = "core/now.html"
    page_title = "Now"
