from django.urls import path

from .views import PostDetailView, PostListView, TagListView, TagPostListView

app_name = "posts"

urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("tags/<slug:slug>/", TagPostListView.as_view(), name="tag"),
    path("<slug:slug>/", PostDetailView.as_view(), name="detail"),
]
