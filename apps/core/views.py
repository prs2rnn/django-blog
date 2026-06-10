from django.views.generic import TemplateView

from ..posts.models import Post


class HomeView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Home".lower()
        context["recent_posts"] = Post.objects.filter(is_published=True).order_by(
            "-created_at"
        )[:5]

        return context


class AboutView(TemplateView):
    template_name = "core/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "About".lower()

        return context


class ContactView(TemplateView):
    template_name = "core/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Contact".lower()

        return context


class UsesView(TemplateView):
    template_name = "core/uses.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Uses".lower()

        return context


class NowView(TemplateView):
    template_name = "core/now.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Now".lower()

        return context
