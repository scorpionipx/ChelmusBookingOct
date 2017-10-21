from django.views import generic

from braces import views

from . import models
from . import forms


class AdvertisementHome(views.LoginRequiredMixin, generic.TemplateView):
    template_name = r'Booking\home.html'


class AdvertisementCreateView(views.LoginRequiredMixin, generic.CreateView):
    """
        Class based view for advertisement creation
    """
    template_name = r'Booking\advertisement_create.html'

    form_class = forms.AdvertisementForm

    model = models.Advertisement

    object_title = 'anunt'

    def form_valid(self, form):
        self.object = form.save(commit=False)

        self.object.save()

        return super(AdvertisementCreateView, self).form_valid(form)


class AdvertisementListView(generic.ListView):

    template_name = r'Booking\advertisement_list.html'

    model = models.Advertisement

    def get_context_data(self, **kwargs):
        context = super(AdvertisementListView, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context


class AdvertisementDetailView(generic.DetailView):

    template_name = r'Booking\advertisement_detail.html'

    model = models.Advertisement

    def get_context_data(self, **kwargs):
        context = super(AdvertisementDetailView, self).get_context_data(**kwargs)
        return context