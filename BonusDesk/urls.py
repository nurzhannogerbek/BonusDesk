from django.conf.urls import (
    url,
    include,
)
from django.contrib import admin
from BonusDesk.views import HomeView
from django.contrib.auth.views import (
    login,
    logout,
)
from dashboard.views import SignupView
from django.core.urlresolvers import reverse_lazy


urlpatterns = [
    # Admin Page
    url(
        r'^admin/',
        admin.site.urls,
        name='admin',
    ),

    # Home Page
    url(
        r'^$',
        HomeView.as_view(),
        name='home',
    ),

    # Links of the "dashboard" application
    url(
        r'^dashboard/',
        include('dashboard.urls')
    ),

    # Signup
    url(
        r'^account/signup/',
        SignupView.as_view(),
        name='account_signup'
    ),

    # Login
    url(
        r'^account/login/$',
        login,
        {
            'template_name': 'account/login.html',
        },
        name='account_login'
    ),

    # Logout
    url(
        r'^account/logout/$',
        logout,
        {
            'next_page': reverse_lazy('home')
        },
        name='account_logout'
    ),

    # url settings of 'django-user-accounts' application
    url(
        r"^account/",
        include("account.urls")
    ),

    # url settings of 'pinax-referrals' application
    url(
        r"^referrals/",
        include("pinax.referrals.urls")
    ),
]
