from django.db.models import F, Q
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Post, Tag


class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = "posts"

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        posts = Post.objects.filter(is_published=True)

        if query:
            posts = posts.filter(
                Q(title__icontains=query)
                | Q(content__icontains=query)
                | Q(tags__name__icontains=query)
            )

        return posts.order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        context["title"] = "posts".lower()
        context["tags"] = Tag.objects.all().order_by("name")
        context["page_desc"] = (
            "Complete archive of blog posts: health, lifestyle, education, and tech insights. Find past articles organized chronologically"
        )
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        session_key = f"viewed_post_{obj.pk}"

        if not self.request.session.get(session_key):
            Post.objects.filter(pk=obj.pk).update(views=F("views") + 1)
            self.request.session[session_key] = True

            obj.refresh_from_db()

        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.title.lower()
        context["page_desc"] = self.object.description
        return context


class TagPostListView(ListView):
    model = Post
    template_name = "posts/tag.html"
    context_object_name = "posts"

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs["slug"])

        return Post.objects.filter(is_published=True, tags=self.tag).order_by(
            "created_at"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.tag
        return context


class TagListView(ListView):
    model = Tag
    template_name = "posts/tags.html"
    context_object_name = "tags"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Tags".lower()
        return context
