
from django.conf.urls import url, include
from django.urls import path

from website import views


urlpatterns = [
    path("login/", views.anon_login, name="anon-login"),
    path("logout/", views.app_logout, name="app-logout"),
    path("", views.app_index, name="app-index"),
]
