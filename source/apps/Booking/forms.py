from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Button

from . import models


class AdvertisementForm(forms.ModelForm):
    """
        Class used to manage HTML form for advertisement creation or updating
    """
    class Meta:
        fields = ('name', 'description', 'main_image', 'image_0', 'image_1', 'image_2', 'image_3', 'image_4', 'county',
                  'city', 'category', 'wifi', 'parking', 'children_playground', 'swimming_pool', 'launch', 'spa',
                  'price', 'site', 'mail', 'phone')
        model = models.Advertisement

    def __init__(self, *args, **kwargs):
        super(AdvertisementForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'description',
            'main_image',
            'image_0',
            'image_1',
            'image_2',
            'image_3',
            'image_4',
            'county',
            'city',
            'category',
            'wifi',
            'parking',
            'children_playground',
            'swimming_pool',
            'launch',
            'spa',
            'price',
            'site',
            'mail',
            'phone',
            ButtonHolder(
                Submit('create', 'Adaugare anunt', css_class='btn-success'),
                Button('cancel', 'Anulare', css_class='btn-danger', onclick="window.history.back()"),
            )
        )



