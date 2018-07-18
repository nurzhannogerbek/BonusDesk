from django.conf.urls import url
from dashboard.views import (
    DashboardView,
    username_autocomplete,
    search_user_information,
    specify_parent,
)
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy


urlpatterns = [
    # Dashboard Page
    url(
        r'^$',
        login_required(login_url=reverse_lazy('account_login'))(DashboardView.as_view()),
        name='dashboard'
    ),

    # Autocomplete in "username" field | Link available to superuser
    url(
        r'^username_autocomplete/$',
        username_autocomplete,
        name='username_autocomplete'
    ),

    # AJAX request which return full user information | Link available to superuser
    url(
        r'^search_user_information/(?P<username>[\w\-]+)/$',
        search_user_information,
        name='search_user_information'
    ),

    # Set parent if user has not registered in the system through the referral link
    url(
        r'^specify_parent/',
        specify_parent,
        name='specify_parent'
    ),
]
