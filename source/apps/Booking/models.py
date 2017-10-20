from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from django.template.defaultfilters import slugify

NAME_MAX_LENGTH = 100
DESCRIPTION_MAX_LENGTH = 1500
PHONE_MAX_LENGTH = 20
SLUG_MAX_LENGTH = 255

DEFAULT_DESCRIPTION = 'no-description'
DEFAULT_PHONE = 'not provided'
DEFAULT_MAIL = 'not provided'
DEFAULT_SITE = 'not provided'


class Advertisement(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='advertisements')
    name = models.CharField(max_length=NAME_MAX_LENGTH, blank=False, null=False)
    description = models.TextField(max_length=DESCRIPTION_MAX_LENGTH, verbose_name='description')
    site = models.URLField(verbose_name='site')
    mail = models.EmailField(verbose_name='email')
    phone = models.CharField(max_length=PHONE_MAX_LENGTH, verbose_name='phone')
    stars = models.IntegerField(verbose_name='stars', default=0, editable=False)

    slug = models.SlugField(max_length=SLUG_MAX_LENGTH)

    class Meta:
        unique_together = ('user', 'name')

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):

        if self.description is None or self.description == '':
            self.description = DEFAULT_DESCRIPTION

        if self.mail is None or self.mail == '':
            self.mail = DEFAULT_MAIL

        if self.site is None or self.site == '':
            self.site = DEFAULT_SITE

        if self.phone is None or self.phone == '':
            self.phone = DEFAULT_PHONE

        self.slug = slugify(str(self.user) + '-' + str(self.name))

    def get_absolute_url(self):
        return reverse('home')






