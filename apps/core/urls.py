from django.urls import path

from .views import AboutView, ContactView, HomeView, NowView, UsesView

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("uses/", UsesView.as_view(), name="uses"),
    path("now/", NowView.as_view(), name="now"),
]
