from __future__ import absolute_import

import django_tables2 as tables
from django_tables2.utils import A
from django.utils.safestring import mark_safe
from django.utils.html import escape

from . import models


class ImageColumn(tables.Column):
    def render(self, value):
        return mark_safe('<img src="/media/%s" height="60" width="100" />' % escape(value))


class AdvertisementTable(tables.Table):
    """
        Class to manage advertisements' table
    """
    # custom columns names
    main_image = ImageColumn(verbose_name='Imagine')
    pk = tables.Column(verbose_name="ID")
    name = tables.LinkColumn('advertisements:DetailAdvertisement', args=[A('slug')], verbose_name='Titlu')
    stars = tables.Column(verbose_name='Stele')
    description = tables.LinkColumn('advertisements:DetailAdvertisement', args=[A('slug')], verbose_name='Description')
    city = tables.Column(verbose_name='Oras')
    county = tables.Column(verbose_name='Judet')
    price = tables.Column(verbose_name="Pret (€)")

    class Meta:
        # table's model
        model = models.Advertisement

        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

        # items to display per page
        per_page = 25

        # fields to display on table
        fields = [
            # 'pk',
            'main_image',
            'name',
            'price',
            'stars',
            'city',
            'county',
        ]

        # custom named fields to hide
        exclude = ('pk', 'description')

