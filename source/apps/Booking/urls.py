from __future__ import absolute_import

from django.conf.urls import url

from . import views

urlpatterns = [

    # Home
    url(r'^$', views.AdvertisementHome.as_view(), name='advertisements-home'),
    url(r'^create_advertisement/', views.AdvertisementCreateView.as_view(), name='CreateAdvertisement'),
]


