from django.views.generic import TemplateView

from apps.core.models import SiteStats

from ..posts.models import Post, Tag


class HomeView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["recent_posts"] = Post.objects.filter(is_published=True).order_by(
            "-created_at"
        )[:5]

        posts = Post.objects.filter(is_published=True)
        tags = Tag.objects

        context["post_count"] = posts.count()
        context["total_words"] = sum(post.words_count for post in posts)
        context["first_post"] = posts.order_by("created_at").first()
        context["visits"] = SiteStats.get().visits
        context["tag_count"] = tags.count()

        return context


class BasePageView(TemplateView):
    page_title = ""
    page_desc = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.page_title.lower()
        context["page_desc"] = self.page_desc
        return context


class AboutView(BasePageView):
    template_name = "core/about.html"
    page_title = "About"
    page_desc = "Learn more about the person behind the blog: my journey, interests, and what inspires me to share these notes."


class ContactView(BasePageView):
    template_name = "core/contact.html"
    page_title = "Contact"
    page_desc = "Have a question or want to collaborate? Find my contact details here and get in touch."


class UsesView(BasePageView):
    template_name = "core/uses.html"
    page_title = "Uses"
    page_desc = "A list of tools, apps, and gear I use daily for work, learning, and maintaining a healthy lifestyle."


class NowView(BasePageView):
    template_name = "core/now.html"
    page_title = "Now"
    page_desc = "My current status: what I’m working on, learning, and exploring at this moment. Updated regularly."
