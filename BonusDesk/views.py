from django.urls import reverse
from django.views.generic import RedirectView


class HomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse("dashboard")
