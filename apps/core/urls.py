from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("uses/", views.UsesView.as_view(), name="uses"),
    path("now/", views.NowView.as_view(), name="now"),
]
