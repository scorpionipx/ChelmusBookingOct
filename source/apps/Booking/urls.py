from __future__ import absolute_import

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [

    # Home
    url(r'^$', views.AdvertisementHome.as_view(), name='advertisements-home'),
    url(r'^create_advertisement/$', views.AdvertisementCreateView.as_view(), name='CreateAdvertisement'),
    url(r'^list_advertisement/$', views.AdvertisementListView.as_view(), name='ListAdvertisement'),
    url(r'^detail_advertisement/(?P<slug>[^\.]+)/$', views.AdvertisementDetailView.as_view(), name='DetailAdvertisement'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


