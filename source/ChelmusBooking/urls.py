from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import HomePageView
from .views import SignUpView
from .views import LoginView
from .views import LogOutView

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Home
    url('^$', HomePageView.as_view(), name='home'),

    # Accounts
    url(r'^accounts/register/$', SignUpView.as_view(), name='signup'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', LogOutView.as_view(), name='logout'),

    # Booking App
    url(r'^advertisements/', include('apps.Booking.urls', namespace='advertisements'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

