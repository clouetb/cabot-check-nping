from django.urls import re_path

from .views import (NPINGCheckCreateView, NPINGCheckUpdateView,
                    duplicate_check)

urlpatterns = [

    re_path(r'^npingcheck/create/',
            view=NPINGCheckCreateView.as_view(),
            name='create-nping-check'),

    re_path(r'^npingcheck/update/(?P<pk>\d+)/',
            view=NPINGCheckUpdateView.as_view(),
            name='update-nping-check'),

    re_path(r'^npingcheck/duplicate/(?P<pk>\d+)/',
            view=duplicate_check,
            name='duplicate-nping-check')

]
