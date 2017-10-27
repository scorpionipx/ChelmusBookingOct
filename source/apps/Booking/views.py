from django.views import generic

from braces import views
from django_tables2 import SingleTableView
from django.db.models import Q

from . import models
from . import forms
from . import tables


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


class AdvertisementTableView(SingleTableView):
    """
        Class based view for Components' table
    """
    template_name = r'Booking\advertisement_table.html'

    model = models.Advertisement
    table_class = tables.AdvertisementTable
    ordering = ['name']

    object_title = "advertisement"

    def get_queryset(self):
        name_ = self.request.GET.get('n')
        if name_ is None:
            name_ = ""

        description_ = self.request.GET.get('d')
        if description_ is None:
            description_ = ""

        city_ = self.request.GET.get('ci')
        if city_ is None:
            city_ = ""

        county_ = self.request.GET.get('co')
        if county_ is None:
            county_ = ""

        stars_ = self.request.GET.get('s')
        if stars_ is None:
            stars_ = ""

        queryset = self.model.objects.filter(Q(name__icontains=name_) & Q(description__icontains=description_) &
                                             Q(city__icontains=city_) & Q(county__icontains=county_)
                                             & Q(stars__icontains=stars_)).order_by('name')
        return queryset






