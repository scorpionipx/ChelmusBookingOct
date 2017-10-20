from __future__ import absolute_import

from django.conf.urls import url

from . import views

urlpatterns = [

    # Home
    url(r'^$', views.AdvertisementsHome.as_view(), name='advertisements-home'),

]


