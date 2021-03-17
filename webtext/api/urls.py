
from django.conf.urls import url, include
from django.urls import path

from api import views


urlpatterns = [
    path("web-analysis/create/", views.create_web_analysis, name="api-create-web-analysis"),
    path("web-analysis/<slug:slug>/details/", views.get_web_analysis_details, name="api-get-web-analysis-details"),
    path("web-analysis/list/", views.get_web_analysis_list, name="api-get-web-analysis-list"),
]
