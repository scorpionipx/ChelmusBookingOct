from django.http import HttpResponse
from django.views import generic

from braces import views

from . import models


class AdvertisementsHome(views.LoginRequiredMixin, generic.TemplateView):
    template_name = 'Booking\home.html'




