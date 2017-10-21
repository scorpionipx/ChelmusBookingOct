from __future__ import absolute_import

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from django.template.defaultfilters import slugify
from . import get_current_user

NAME_MAX_LENGTH = 100
DESCRIPTION_MAX_LENGTH = 1500
PHONE_MAX_LENGTH = 20
SLUG_MAX_LENGTH = 255

DEFAULT_DESCRIPTION = 'no-description'
DEFAULT_PHONE = 'not provided'
DEFAULT_MAIL = 'not provided'
DEFAULT_SITE = 'not provided'


class Advertisement(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=True, related_name='advertisements',
                             verbose_name='author')

    name = models.CharField(max_length=NAME_MAX_LENGTH, blank=False, null=False, verbose_name='Titlu')
    description = models.TextField(max_length=DESCRIPTION_MAX_LENGTH, blank=True,
                                   verbose_name='Descriere')

    date_created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='created')

    site = models.URLField(blank=True, verbose_name='Site')
    mail = models.EmailField(blank=True, verbose_name='Email')
    phone = models.CharField(max_length=PHONE_MAX_LENGTH, blank=True, verbose_name='Telefon')
    stars = models.IntegerField(blank=True, default=0, editable=False, verbose_name='Voturi')

    slug = models.SlugField(max_length=SLUG_MAX_LENGTH, blank=True, editable=False)

    class Meta:
        unique_together = ('user', 'name')
        ordering = ('date_created', )

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):

        if self.description is None or self.description == '':
            self.description = DEFAULT_DESCRIPTION
            print(self.description)

        if self.mail is None or self.mail == '':
            self.mail = DEFAULT_MAIL

        if self.site is None or self.site == '':
            self.site = DEFAULT_SITE

        if self.phone is None or self.phone == '':
            self.phone = DEFAULT_PHONE

        current_request_user = get_current_user.get_thread_user()
        self.user = current_request_user.user
        self.slug = slugify(str(self.user.username) + '-' + str(self.name))
        
        super(Advertisement, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('home')






