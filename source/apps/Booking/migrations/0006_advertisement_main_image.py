# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-21 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0005_auto_20171021_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='main_image',
            field=models.ImageField(blank=True, default=None, help_text='Imaginea de prezentare', null=True, upload_to='profiles/%Y/%m/%d', verbose_name='Profile image'),
        ),
    ]