from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("tags/", views.TagListView.as_view(), name="tags"),
    path("tags/<slug:slug>/", views.TagPostListView.as_view(), name="tag"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
]
